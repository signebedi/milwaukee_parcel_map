import geopandas as gpd

# Load the shapefile
parcels = gpd.read_file('data/V900_Wisconsin_Parcels_MILWAUKEE.shp')

# Inspect the data
print(parcels.head())