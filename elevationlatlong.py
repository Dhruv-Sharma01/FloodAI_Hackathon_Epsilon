import requests

def get_elevation(lat, lon):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    response = requests.get(url)
    elevation_data = response.json()
    if 'results' in elevation_data:
        elevation = elevation_data['results'][0]['elevation']
        print(f"Elevation at ({lat}, {lon}): {elevation} meters")
    else:
        print("Error fetching elevation data")

# Example latitude and longitude
latitude = 19.0760
longitude = 72.8777

get_elevation(latitude, longitude)
