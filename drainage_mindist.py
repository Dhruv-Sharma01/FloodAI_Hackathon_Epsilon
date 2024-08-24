import pandas as pd
from scipy.spatial import cKDTree

def calculate_nearest_distances(elevation_csv_path, drainage_csv_path, output_csv_path):
    # Load the elevation data and drainage coordinates from the CSV files
    elevation_data = pd.read_csv(elevation_csv_path)
    drainage_data = pd.read_csv(drainage_csv_path)

    # Extract coordinates
    elevation_coords = elevation_data[['Latitude', 'Longitude']].values
    drainage_coords = drainage_data[['latitude', 'longitude']].values

    # Use scipy's cKDTree for fast nearest neighbor lookup
    tree = cKDTree(drainage_coords)

    # Find the nearest drainage point for each elevation point
    distances, indices = tree.query(elevation_coords, k=1)
    elevation_data['Nearest_Drainage_Distance'] = distances*111

    # Save the enhanced dataset with distances to a new CSV file
    elevation_data.to_csv(output_csv_path, index=False)

# Define file paths
elevation_csv_path = 'mumbai_elevation.csv'
drainage_csv_path = 'drainage_lat_long.csv'
output_csv_path = 'lat_long_drainage_mindist1.csv'

# Function call
calculate_nearest_distances(elevation_csv_path, drainage_csv_path, output_csv_path)
