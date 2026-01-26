#!/usr/bin/env python3
"""
Load wedding guest locations from Google Sheet and create an interactive map.

This script:
1. Loads guest data from a Google Sheet
2. Extracts location information
3. Creates an interactive folium map with guest locations

Authentication:
- For read-only access (public or shared sheet): No authentication needed
- For private sheets: Requires Google API credentials (see setup instructions below)

Setup Instructions:
====================

OPTION 1: Public or Shared Google Sheet (No authentication needed)
- Simply run the script if the sheet is accessible via the URL

OPTION 2: Private Sheet (Requires Authentication)
- Create a Google Cloud project: https://console.cloud.google.com/
- Enable Google Sheets API
- Create a Service Account and download JSON credentials
- Store credentials in: .env or config.env
- Add to .gitignore to prevent credential leakage

Environment Variables:
- GOOGLE_SHEET_ID: The sheet ID extracted from the URL
- GOOGLE_CREDENTIALS_PATH: Path to service account JSON file (if needed)

"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

try:
    import gspread
    import folium
    import geopandas as gpd
    import pandas as pd
    import google.auth
    from google.oauth2 import service_account
    from geopy.distance import geodesic
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip install gspread folium geopandas pandas python-dotenv google-auth geopy")
    sys.exit(1)

# Load environment variables
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    print("Note: No .env file found. Using public sheet access.")

# Google Sheet URL and ID
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/106BZ1Jh1htdV9E-U0ZbRwqu8nxmpHdV7iQd3MUd9nXw"
GOOGLE_SHEET_ID = "106BZ1Jh1htdV9E-U0ZbRwqu8nxmpHdV7iQd3MUd9nXw"
GID = "669383229"  # Sheet tab ID


def load_sheet_public():
    """
    Load Google Sheet using public URL (no authentication).
    Note: Sheet must be shared with "Anyone with the link" or "Public" access.
    """
    try:
        # For public sheets, we can use pandas + gspread without auth
        url = f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}/export?format=csv&gid={GID}"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error loading public sheet: {e}")
        return None


def load_sheet_authenticated():
    """
    Load Google Sheet using gcloud application-default credentials.
    This uses credentials from: gcloud auth application-default login
    """
    try:
        # Use gcloud application-default credentials
        creds, _ = google.auth.default(
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        gc = gspread.Client(auth=creds)
        sheet = gc.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sheet.get_worksheet_by_id(int(GID))
        df = pd.DataFrame(worksheet.get_all_records())
        return df

    except PermissionError as e:
        print(f"⚠ Permission Error: Check if Google Sheets API is enabled")
        print(f"  Enable API: https://console.cloud.google.com/apis/library/sheets.googleapis.com")
        return None
    except Exception as e:
        print(f"Error loading authenticated sheet: {e}")
        return None


def load_guest_data():
    """
    Load guest data from Google Sheet.
    Uses authenticated access via gcloud credentials.
    """
    print("Attempting to load Google Sheet...")

    # Try authenticated access
    df = load_sheet_authenticated()
    if df is not None and not df.empty:
        print(f"✓ Loaded sheet successfully ({len(df)} rows)")
        return df

    print("✗ Failed to load Google Sheet")
    return None


def prepare_location_data(df):
    """
    Prepare location data from the dataframe.
    Handles various coordinate formats.
    """
    print("\nPreparing location data...")
    
    # Clean up column names (remove trailing/leading whitespace)
    df.columns = df.columns.str.strip()
    print(f"Available columns: {df.columns.tolist()}")

    # Look for coordinate columns in various formats
    location_cols = [col for col in df.columns if 'location' in col.lower() or 'address' in col.lower()]
    lat_cols = [col for col in df.columns if 'lat' in col.lower()]
    lon_cols = [col for col in df.columns if 'lon' in col.lower() or 'long' in col.lower()]
    coord_cols = [col for col in df.columns if 'coord' in col.lower() or 'position' in col.lower()]

    print(f"Location columns: {location_cols}")
    print(f"Latitude columns: {lat_cols}")
    print(f"Longitude columns: {lon_cols}")
    print(f"Coordinate columns: {coord_cols}")

    # If we have separate lat/lon columns, we're done
    if lat_cols and lon_cols:
        df['latitude'] = pd.to_numeric(df[lat_cols[0]], errors='coerce')
        df['longitude'] = pd.to_numeric(df[lon_cols[0]], errors='coerce')
        return df

    # If we have combined coordinates (e.g., "lat, lon" or "lon,lat"), parse them
    if coord_cols:
        coord_col = coord_cols[0]
    else:
        # Check if 'Koordinates' exists (German spelling)
        if 'Koordinates' in df.columns:
            coord_col = 'Koordinates'
        else:
            coord_col = None
    
    if coord_col is not None:
        print(f"\nParsing coordinates from '{coord_col}' column...")
        
        def parse_coordinates(coord_str):
            """Parse comma-separated coordinates."""
            if pd.isna(coord_str):
                return None, None
            try:
                # Convert to string and strip whitespace
                coord_str = str(coord_str).strip()
                # Split by comma
                parts = coord_str.split(',')
                if len(parts) >= 2:
                    lat = float(parts[0].strip())
                    lon = float(parts[1].strip())
                    return lat, lon
            except (ValueError, AttributeError):
                pass
            return None, None

        df[['latitude', 'longitude']] = df[coord_col].apply(
            lambda x: pd.Series(parse_coordinates(x))
        )
        
        # Remove rows with missing coordinates
        df = df.dropna(subset=['latitude', 'longitude'])
        print(f"✓ Parsed {len(df)} locations with valid coordinates")
        return df

    return df


def calculate_distances_to_alte_schule(df):
    """
    Calculate distance from each location to "Alte Schule".
    Returns dataframe with added 'Distance to Alte Schule (m)' column.
    """
    print("\nCalculating distances to 'Alte Schule'...")
    
    # Find "Alte Schule" location
    alte_schule_rows = df[df['Unterkunft'].str.strip() == 'Alte Schule']
    
    if alte_schule_rows.empty:
        print("⚠ 'Alte Schule' not found in data")
        return df
    
    alte_schule_lat = alte_schule_rows.iloc[0]['latitude']
    alte_schule_lon = alte_schule_rows.iloc[0]['longitude']
    alte_schule_coords = (alte_schule_lat, alte_schule_lon)
    
    print(f"✓ Found 'Alte Schule' at ({alte_schule_lat:.6f}, {alte_schule_lon:.6f})")
    
    # Calculate distance to all locations
    def calc_distance(row):
        if pd.isna(row['latitude']) or pd.isna(row['longitude']):
            return None
        location_coords = (row['latitude'], row['longitude'])
        # Distance in meters
        distance = geodesic(alte_schule_coords, location_coords).meters
        return distance
    
    df['Distance to Alte Schule (m)'] = df.apply(calc_distance, axis=1)
    print(f"✓ Calculated distances for {df['Distance to Alte Schule (m)'].notna().sum()} locations")
    
    return df


def create_map(df, output_file=None):
    """
    Create an interactive folium map with guest locations.
    - Red marker: Alte Schule
    - Green marker: Sportplatz
    - Blue marker: All other locations
    - Hover shows: Unterkunft name and website (if available)
    """
    print(f"\nCreating map...")
    
    # Set default output path to web/data/maps/
    if output_file is None:
        output_path = Path(__file__).parent.parent / "docs" / "data" / "maps"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "guest_locations_map.html"
    else:
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)

    # Create base map (centered on approximate center of data)
    if len(df) == 0:
        print("No data to plot")
        return None

    # Try to get lat/lon columns
    lat_col = next((col for col in df.columns if 'lat' in col.lower()), None)
    lon_col = next((col for col in df.columns if 'lon' in col.lower() or 'long' in col.lower()), None)

    if lat_col is None or lon_col is None:
        print("Error: Could not find latitude/longitude columns in sheet")
        print("Please ensure your Google Sheet has 'latitude' and 'longitude' columns")
        return None

    # Create map
    center_lat = df[lat_col].mean()
    center_lon = df[lon_col].mean()

    map_obj = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=13,
        tiles="OpenStreetMap"
    )

    # Add markers for each location
    for idx, row in df.iterrows():
        lat = row[lat_col]
        lon = row[lon_col]
        
        # Get location name from Unterkunft column
        unterkunft = row.get('Unterkunft', f'Location {idx}')
        if pd.isna(unterkunft):
            unterkunft = f'Location {idx}'
        unterkunft = str(unterkunft).strip()
        
        # Get website if available
        website = row.get('Website', '')
        if pd.isna(website):
            website = ''
        website = str(website).strip()
        
        # Get distance if available
        distance = row.get('Distance to Alte Schule (m)', None)
        
        # Get prive level range if available
        prive_level = row.get('prive level range', '')
        if pd.isna(prive_level):
            prive_level = ''
        prive_level = str(prive_level).strip()
        
        # Create formatted HTML popup with each field on separate row
        popup_html = f"<b>{unterkunft}</b><br>"
        
        # Add website link if available
        if website:
            popup_html += f"Website: <a href='{website}' target='_blank'>{website}</a><br>"
        
        # Add distance to Alte Schule if available
        if pd.notna(distance):
            popup_html += f"Distance to Alte Schule: {distance:.0f}m<br>"
        
        # Add prive level range if available
        if prive_level:
            popup_html += f"Price Range: {prive_level}<br>"
        
        # Create tooltip with multiple lines - each field on separate row
        # Note: Website is NOT shown in tooltip (only on popup)
        tooltip_html = f"<b>{unterkunft}</b><br>"
        if prive_level:
            tooltip_html += f"Price Range: {prive_level}<br>"
        if pd.notna(distance):
            tooltip_html += f"Distance to Alte Schule: {distance:.0f}m"
        
        # Determine marker color based on Unterkunft name
        if unterkunft == "Alte Schule":
            color = 'red'
            icon = 'home'
        elif unterkunft == "Sportplatz":
            color = 'green'
            icon = 'tree'
        else:
            color = 'blue'
            icon = 'info-sign'

        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=tooltip_html,
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(map_obj)

    # Save map
    map_obj.save(output_file)
    print(f"✓ Map saved to {output_file}")
    return map_obj


def main():
    """Main execution."""
    print("=" * 60)
    print("Wedding Guest Location Mapper")
    print("=" * 60)

    # Load data
    df = load_guest_data()
    if df is None:
        print("\n⚠ Failed to load data. Check your configuration.")
        return

    # Prepare data
    df = prepare_location_data(df)
    print("\nDataFrame preview:")
    print(df.head())

    # Calculate distances to Alte Schule
    df = calculate_distances_to_alte_schule(df)
    
    # Create map
    map_obj = create_map(df)
    if map_obj is None:
        print("\n⚠ Failed to create map.")
        return

    # Save updated data with distances to data/temp/
    output_csv = Path(__file__).parent.parent / "data" / "temp" / "accommodations_with_distances.csv"
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"✓ Data saved to {output_csv}")

    print("\n" + "=" * 60)
    print("✓ Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
