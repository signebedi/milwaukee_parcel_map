import geopandas as gpd

# Load the shapefile
parcels = gpd.read_file('path_to_your_file.shp')

# Inspect the data
print(parcels.head())