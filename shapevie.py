import geopandas as gpd
import matplotlib.pyplot as plt

# Path to your shapefile
shapefile_path = "Surat Images/Surat (Tapi basin)/Results/Results/Surat_Validation_2006_Flood_elements_028.shp"

# Load the shapefile
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile
fig, ax = plt.subplots(figsize=(10, 10))  # Adjust the figure size as needed
gdf.plot(ax=ax, color='lightblue', edgecolor='black')  # Customize colors as desired

# Optional: Enhancements
ax.set_title('Shapefile Map')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.grid(True)  # Enable grid if needed

# Show the plot
plt.show()
