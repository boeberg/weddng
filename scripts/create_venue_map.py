#!/usr/bin/env python3
"""
Create a national-level map showing the Alte Schule venue location.
Generates an interactive HTML map using folium with venue coordinates loaded from accommodations CSV.
"""

import os
import sys
import csv
from pathlib import Path

try:
    import folium
except ImportError:
    print("Error: folium package not installed.")
    print("Run: pip install folium")
    sys.exit(1)


def load_venue_coordinates():
    """
    Load Alte Schule coordinates from accommodations CSV file.
    Returns venue name, coordinates [lat, lon], and location name.
    """
    script_dir = Path(__file__).parent.parent
    csv_path = script_dir / 'data' / 'temp' / 'accommodations_with_distances.csv'
    
    if not csv_path.exists():
        raise FileNotFoundError(f"Accommodations CSV not found at {csv_path}")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Unterkunft'].strip() == 'Alte Schule':
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                venue_coords = [latitude, longitude]
                
                # Extract location from address if available
                location = "Warnkenhagen, Germany"
                
                return 'Alte Schule', venue_coords, location
    
    raise ValueError("Alte Schule not found in accommodations CSV")


def create_venue_map():
    """
    Create an interactive map showing the Alte Schule venue location.
    The map is centered on the venue with a marker at the coordinates.
    """
    
    # Load venue coordinates from CSV
    venue_name, venue_coords, location = load_venue_coordinates()
    
    # Create map centered on the venue location
    wedding_map = folium.Map(
        location=venue_coords,  # Center on Alte Schule
        zoom_start=13,  # Closer zoom level for the area
        tiles='OpenStreetMap',
        prefer_canvas=True
    )
    
    # Add marker for the venue
    folium.Marker(
        location=venue_coords,
        popup=f"<b>{venue_name}</b><br>{location}",
        tooltip=venue_name,
        icon=folium.Icon(color='red', icon='heart', prefix='fa'),
    ).add_to(wedding_map)
    
    # Add a circle to highlight the venue area
    folium.Circle(
        location=venue_coords,
        radius=5000,  # 5km radius
        color='red',
        fill=True,
        fillColor='red',
        fillOpacity=0.1,
        weight=2,
        opacity=0.7
    ).add_to(wedding_map)
    
    return wedding_map


def main():
    """Main function to generate and save the map."""
    
    # Determine output path
    script_dir = Path(__file__).parent.parent
    maps_dir = script_dir / 'docs' / 'data' / 'maps'
    maps_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = maps_dir / 'venue_location_map.html'
    
    print(f"Creating venue location map...")
    
    # Generate map
    wedding_map = create_venue_map()
    
    # Save map
    wedding_map.save(str(output_file))
    print(f"✓ Map saved to: {output_file}")


if __name__ == '__main__':
    main()
