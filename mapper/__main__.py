import os
import geopandas as gpd
from shapely.geometry import box
from pyproj import Transformer
import folium

# transformer to convert from EPSG:4326 to EPSG:3071
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3071")

# approximate values for downtown Milwaukee
minx, miny = transformer.transform(43.0285, -87.9280)
maxx, maxy = transformer.transform(43.0490, -87.8980)

bounds = box(minx, miny, maxx, maxy)

if 'DEV' in os.environ and os.environ['DEV'] == '1':
    dev = True
    # If in development mode, load only a sample of the data
    parcels = gpd.read_file('data/V900_Wisconsin_Parcels_MILWAUKEE.shp', bbox=bounds)
    print(parcels.head())
    print(parcels.crs)
else:
    dev = False
    # Otherwise, load all the data
    parcels = gpd.read_file('data/V900_Wisconsin_Parcels_MILWAUKEE.shp')

# Convert to GeoJSON
parcels_json = parcels.to_json()

# Create a map centered at an approximate location in downtown Milwaukee
m = folium.Map(location=[43.0389, -87.9065], zoom_start=13)

# Add the parcel data to the map
folium.GeoJson(parcels_json).add_to(m)

# Create output dir if it doesn't exist
directory_name = 'output'
os.makedirs(directory_name, exist_ok=True)

# Save the map to a file
m.save(f'output/{"dev_" if dev else ""}map.html')