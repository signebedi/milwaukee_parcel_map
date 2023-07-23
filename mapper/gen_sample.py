from shapely.geometry import box
from pyproj import Transformer
import geopandas as gpd

# transformer to convert from EPSG:4326 to EPSG:3071
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3071")

# approximate values for downtown Milwaukee
minx, miny = transformer.transform(43.0285, -87.9280)
maxx, maxy = transformer.transform(43.0490, -87.8980)

bounds = box(minx, miny, maxx, maxy)

# Load the parcels within the bounding box
parcels = gpd.read_file('data/V900_Wisconsin_Parcels_MILWAUKEE.shp', bbox=bounds)

# Inspect the data
print(parcels.head())


