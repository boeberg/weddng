#!/usr/bin/env python3
"""
Create a national-level map showing the Alte Schule venue location in Bad Sobernheim, Germany.
Generates an interactive HTML map using folium.
"""

import os
import sys
from pathlib import Path

try:
    import folium
except ImportError:
    print("Error: folium package not installed.")
    print("Run: pip install folium")
    sys.exit(1)


def create_venue_map():
    """
    Create an interactive map showing the Alte Schule venue location.
    The map is centered on Germany with a marker at Bad Sobernheim.
    """
    
    # Alte Schule location coordinates (Bad Sobernheim, Germany)
    venue_name = "Alte Schule"
    venue_coords = [49.6544, 7.6575]  # Bad Sobernheim coordinates
    
    # Create map centered on Germany
    wedding_map = folium.Map(
        location=[51.1657, 10.4515],  # Center of Germany
        zoom_start=7,
        tiles='OpenStreetMap',
        prefer_canvas=True
    )
    
    # Add marker for the venue
    folium.Marker(
        location=venue_coords,
        popup=f"<b>{venue_name}</b><br>Bad Sobernheim, Germany",
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
