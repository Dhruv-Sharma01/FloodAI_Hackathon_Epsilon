import folium
from folium.plugins import MarkerCluster
from branca.colormap import linear
import pandas as pd

# Load the data
data_path = 'Flood_Risk_Assessment_Results.xlsx'
data = pd.read_excel(data_path)

# It appears that latitude and longitude may be swapped or mislabeled
# Swap them if necessary or verify their correctness
data.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'}, inplace=True)

# Create a colormap
colormap = linear.YlOrRd_09.scale(data['FRI'].min(), data['FRI'].max())
colormap.caption = 'Flood Risk Index (FRI)'

# Create a Folium map centered around the average latitude and longitude
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=11)

# Initialize MarkerCluster
marker_cluster = MarkerCluster().add_to(m)

# Plot each point on the map using the color from the colormap
for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=8,  # Adjust the size as needed
        color=colormap(row['FRI']),  # Color depends on the FRI score
        fill=True,
        fill_color=colormap(row['FRI']),
        fill_opacity=0.7,
        popup=f"FRI: {row['FRI']:.2f} - {row['Risk Category']}"
    ).add_to(marker_cluster)

colormap.add_to(m)  # Add the colormap to the map

# Save the map to an HTML file
output_html = 'flood_risk_map_with_clusters.html'
m.save(output_html)

print(f"Map has been saved to {output_html}")
