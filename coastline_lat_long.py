import geopandas as gpd

# Load your shapefile
gdf = gpd.read_file("coastline/coastl_ind.shp")

# Convert the geometry in the GeoDataFrame to latitude and longitude (if it's not in lat-long already)
# This step assumes your data might not be in latitude-longitude format. If it is, you can skip this conversion.
gdf = gdf.to_crs(epsg=4326)

# Extract latitude and longitude coordinates
gdf['longitude'] = gdf.geometry.centroid.x
gdf['latitude'] = gdf.geometry.centroid.y

# Print the extracted coordinates
print(gdf[['longitude', 'latitude']])

# Optionally, save the coordinates to a CSV file
gdf[['longitude', 'latitude']].to_csv("coordinates.csv", index=False)