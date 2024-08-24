import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
from folium import LinearColormap

# Load the data from CSV
data_path = 'lat_long_drainage_mindist.csv'
data = pd.read_csv(data_path)

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(
    data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))

# Set the coordinate reference system to latitude/longitude
gdf.set_crs(epsg=4326, inplace=True)

# Create a base folium map centered around the mean location of your points
m = folium.Map(location=[gdf['Latitude'].mean(), gdf['Longitude'].mean()], zoom_start=6)

# Define a colormap
colormap = LinearColormap(colors=['blue', 'green', 'yellow', 'red'],
                          vmin=gdf['Nearest_Drainage_Distance'].min(),
                          vmax=gdf['Nearest_Drainage_Distance'].max(),
                          caption="Minimum Distance to Drainage")

# Use MarkerCluster to handle overlapping points
marker_cluster = MarkerCluster().add_to(m)

# Add points to the map
for _, row in gdf.iterrows():
    color = colormap(row['Nearest_Drainage_Distance'])  # Get the color from the colormap
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        popup=f"Nearest Drainage Distance: {row['Nearest_Drainage_Distance']} meters",
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(marker_cluster)

# Add the color legend to the map
colormap.add_to(m)

# Save the map to an HTML file
m.save('drainage_map.html')

# Display the map in a Jupyter notebook (optional)
# m
