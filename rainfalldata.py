import pandas as pd
import requests

# Load the data from the CSV file
data_path = 'lat_long_drainage_mindist1.csv'
data = pd.read_csv(data_path)

# Define the base URL for the NASA POWER API
base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"

# Define the date range and parameters for the API request
start_date = "20220501"  # Start date in YYYYMMDD format
end_date = "20221031"    # End date in YYYYMMDD format

# Initialize a dictionary to hold the data
rainfall_dict = {}

# Loop through each row in the DataFrame
for index, row in data.iterrows():
    latitude = row['Latitude']
    longitude = row['Longitude']
    params = {
        "start": start_date,
        "end": end_date,
        "latitude": latitude,
        "longitude": longitude,
        "community": "RE",
        "parameters": "PRECTOT",
        "format": "CSV",
        "time-standard": "LST"
    }

    # Make the request
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Process the response text
        lines = response.text.split('\n')
        data_lines = lines[10:]  # Skip header lines if necessary

        # Extract date and rainfall data
        rainfall_data = []
        dates = []
        for line in data_lines:
            if line.strip():  # Ensure the line is not empty
                parts = line.split(',')
                dates.append(parts[0])  # Assuming the date is in the first column
                rainfall_data.append(float(parts[3]))  # Assuming the rainfall data is in the fourth column

        # Store the rainfall data in the dictionary
        location_key = f"{latitude}_{longitude}"
        rainfall_dict[location_key] = rainfall_data
        print("done")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for ({latitude}, {longitude}): {e}")

    # Optional: Add a delay to avoid hitting request limits
    # import time
    # time.sleep(1)

# Convert the dictionary to a DataFrame
rainfall_df = pd.DataFrame.from_dict(rainfall_dict, orient='index', columns=dates)

# Save the DataFrame to a CSV file
rainfall_df.to_csv("rainfall_data.csv")
