# MMRDA\MMRDA_Manual.shp

import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import nearest_points

# Load the shapefile that contains land boundaries
land_shapefile = "path_to_shapefile_of_land_boundaries.shp"
land = gpd.read_file(land_shapefile)

# Load the shapefile or dataset that contains water boundaries (if available)
# If you don't have this, you can infer water as anything outside the land polygons
# water_shapefile = "path_to_shapefile_of_water_boundaries.shp"
# water = gpd.read_file(water_shapefile)

# Given latitude and longitude
latitude = 19.0760
longitude = 72.8777
point = Point(longitude, latitude)

# Find the nearest point on the land boundary (this is the closest land point)
nearest_land_point = nearest_points(point, land.unary_union)[1]

# Calculate the distance to the nearest land point (in degrees or meters, depending on CRS)
distance_to_land = point.distance(nearest_land_point)

# If you have a water boundary, find the closest point in the water
# nearest_water_point = nearest_points(point, water.unary_union)[1]
# distance_to_water = point.distance(nearest_water_point)

# Output the nearest point in the sea (inferred as outside land)
print(f"Nearest point on land: {nearest_land_point}")
print(f"Distance to nearest land point: {distance_to_land} degrees")

# If you had water boundaries, you could also output this:
# print(f"Nearest point in water: {nearest_water_point}")
# print(f"Distance to nearest water point: {distance_to_water} degrees")
