import requests
import folium
import pandas as pd

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


# Load the elevation data from the provided CSV file
elevation_data = pd.read_csv("elevation (1).csv")

# Initialize the map centered at Mumbai
mumbai_map = folium.Map(location=[19.0760, 72.8777], zoom_start=11)

# Plot population data on the map
for area in areas:
    lat, lon = get_lat_long_opencage(area["area"] + ", Mumbai", api_key)
    if lat and lon:
        folium.CircleMarker(
            location=(lat, lon),
            radius=area["population"] / 100000,  # Scale radius by population
            popup=f"{area['area']} (Population: {area['population']})",
            color="blue",
            fill=True,
            fill_color="blue"
        ).add_to(mumbai_map)

# Plot elevation data on the map
for _, area in elevation_data.iterrows():
    # Scale factor for visibility, adjust as necessary
    scale_factor = 1
    radius = max(5, area['Elevation'] * scale_factor)
    folium.CircleMarker(
        location=(area["Latitude"], area["Longitude"]),
        radius=radius,
        popup=f"Elevation: {area['Elevation']} m",
        color="red",
        fill=True,
        fill_color="red"
    ).add_to(mumbai_map)

# Save the map to an HTML file
mumbai_map.save("mumbai_population_map_with_elevation.html")



# import requests
# import folium

# # Function to get latitude and longitude using OpenCage API
# def get_lat_long_opencage(area_name, api_key):
#     endpoint = "https://api.opencagedata.com/geocode/v1/json"
#     params = {
#         "q": area_name,
#         "key": api_key,
#         "limit": 1
#     }
#     response = requests.get(endpoint, params=params)
#     data = response.json()
#     if data['results']:
#         lat_long = data['results'][0]['geometry']
#         return lat_long['lat'], lat_long['lng']
#     else:
#         return None, None

# # Your OpenCage API Key
# api_key = "2675d41eedaa402db5270c10a367efcc"

# # List of areas with population
# areas = [
#     {"ward": "A", "area": "Colaba", "population": 210847},
#     {"ward": "B", "area": "Sanhurst Road", "population": 140633},
#     {"ward": "C", "area": "Marine Lines", "population": 202922},
#     {"ward": "D", "area": "Grant Road", "population": 382841},
#     {"ward": "E", "area": "Byculla", "population": 440335},
#     {"ward": "F South", "area": "Parel", "population": 396122},
#     {"ward": "F North", "area": "Matunga", "population": 524393},
#     {"ward": "G South", "area": "Elphinstone", "population": 457931},
#     {"ward": "G North", "area": "Dadar/Plaza", "population": 582007},
#     {"ward": "H East", "area": "Khar/Santacruz", "population": 580835},
#     {"ward": "H West", "area": "Bandra", "population": 337391},
#     {"ward": "K East", "area": "Andheri (East)", "population": 810002},
#     {"ward": "K West", "area": "Andheri (West)", "population": 700680},
#     {"ward": "L", "area": "Kurla", "population": 778218},
#     {"ward": "M East", "area": "Chembur East", "population": 674850},
#     {"ward": "M West", "area": "Chembur West", "population": 414040},
#     {"ward": "N", "area": "Ghatkopar", "population": 619556},
#     {"ward": "P South", "area": "Goregaon", "population": 437849},
#     {"ward": "P North", "area": "Malad", "population": 796775},
#     {"ward": "R South", "area": "Kandivalli", "population": 589886},
#     {"ward": "R Central", "area": "Borivali West", "population": 513077},
#     {"ward": "R North", "area": "Dahiser", "population": 363827},
#     {"ward": "S", "area": "Bhandup", "population": 691227},
#     {"ward": "T", "area": "Mulund", "population": 330195},
# ]

# # Initialize the map centered at Mumbai
# mumbai_map = folium.Map(location=[19.0760, 72.8777], zoom_start=11)

# # Loop through each area to get lat/long and plot it on the map
# for area in areas:
#     lat, lon = get_lat_long_opencage(area["area"] + ", Mumbai", api_key)
#     if lat and lon:
#         folium.CircleMarker(
#             location=(lat, lon),
#             radius=area["population"] / 100000,  # Scale radius by population
#             popup=f"{area['area']} (Population: {area['population']})",
#             color="blue",
#             fill=True,
#             fill_color="blue"
#         ).add_to(mumbai_map)

# # Save the map to an HTML file
# mumbai_map.save("mumbai_population_map.html")
# # 