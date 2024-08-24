import geopandas as gpd
import matplotlib.pyplot as plt
import requests

# Function to get latitude and longitude using OpenCage API
def get_lat_long_opencage(area_name, api_key):
    endpoint = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": area_name,
        "key": api_key,
        "limit": 1
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    if data['results']:
        lat_long = data['results'][0]['geometry']
        return lat_long['lat'], lat_long['lng']
    else:
        return None, None

# Your OpenCage API Key
api_key = "2675d41eedaa402db5270c10a367efcc"

# List of areas with population
areas = [
    {"ward": "A", "area": "Colaba", "population": 210847},
    {"ward": "B", "area": "Sanhurst Road", "population": 140633},
    {"ward": "C", "area": "Marine Lines", "population": 202922},
    {"ward": "D", "area": "Grant Road", "population": 382841},
    {"ward": "E", "area": "Byculla", "population": 440335},
    {"ward": "F South", "area": "Parel", "population": 396122},
    {"ward": "F North", "area": "Matunga", "population": 524393},
    {"ward": "G South", "area": "Elphinstone", "population": 457931},
    {"ward": "G North", "area": "Dadar/Plaza", "population": 582007},
    {"ward": "H East", "area": "Khar/Santacruz", "population": 580835},
    {"ward": "H West", "area": "Bandra", "population": 337391},
    {"ward": "K East", "area": "Andheri (East)", "population": 810002},
    {"ward": "K West", "area": "Andheri (West)", "population": 700680},
    {"ward": "L", "area": "Kurla", "population": 778218},
    {"ward": "M East", "area": "Chembur East", "population": 674850},
    {"ward": "M West", "area": "Chembur West", "population": 414040},
    {"ward": "N", "area": "Ghatkopar", "population": 619556},
    {"ward": "P South", "area": "Goregaon", "population": 437849},
    {"ward": "P North", "area": "Malad", "population": 796775},
    {"ward": "R South", "area": "Kandivalli", "population": 589886},
    {"ward": "R Central", "area": "Borivali West", "population": 513077},
    {"ward": "R North", "area": "Dahiser", "population": 363827},
    {"ward": "S", "area": "Bhandup", "population": 691227},
    {"ward": "T", "area": "Mulund", "population": 330195},
]

# Load the shapefile of Mumbai
shapefile_path = "MMRDA/MMRDA_Manual.shp"
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile using GeoPandas
ax = gdf.plot(figsize=(10, 10), color='white', edgecolor='black')

# Loop through each area to get lat/long, print them, and plot them on the map
for area in areas:
    lat, lon = get_lat_long_opencage(area["area"] + ", Mumbai", api_key)
    if lat and lon:
        # Print latitude and longitude
        print(f"Area: {area['area']}, Ward: {area['ward']}, Latitude: {lat}, Longitude: {lon}")
        # Plot the point on the map
        plt.scatter(lon, lat, s=area["population"] / 1000, color='blue', alpha=0.5)

# Customize the plot
plt.title('Population Distribution in Mumbai')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()
