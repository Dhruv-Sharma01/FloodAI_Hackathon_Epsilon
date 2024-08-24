import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
shapefile_path = "coastline/coastl_ind.shp"
gdf = gpd.read_file(shapefile_path)

# View basic information about the shapefile
print(gdf.head())        # View the first few rows of the GeoDataFrame
print(gdf.crs)           # View the coordinate reference system (CRS)
print(gdf.columns)       # View the columns in the shapefile attribute table

# Plot the shapefile
gdf.plot()

# Customize the plot
plt.title("Shapefile Visualization")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)

# Show the plot
plt.show()
