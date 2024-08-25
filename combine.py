import pandas as pd
import numpy as np

# Load the data
file_path = 'Combined_Data.xlsx'
data = pd.read_excel(file_path)

# Normalize the data (min-max scaling)
def normalize(df):
    return (df - df.min()) / (df.max() - df.min())

data['Normalized Elevation'] = normalize(data['Elevation'])
data['Normalized Distance'] = normalize(data['Nearest_Drainage_Distance'])
data['Normalized Rainfall'] = normalize(data['Annual Average Rainfall'])

# Define AHP weights based on expert judgment
weights = {
    'Elevation': 0.3, 
    'Distance': 0.4, 
    'Rainfall': 0.3
}

# Calculate the Flood Risk Index (FRI) using weighted sum model
data['FRI'] = (data['Normalized Elevation'] * weights['Elevation'] +
               data['Normalized Distance'] * weights['Distance'] +
               data['Normalized Rainfall'] * weights['Rainfall'])

# Define risk categories based on FRI
def classify_risk(fri):
    if fri < 0.2:
        return 'Very Low'
    elif fri < 0.4:
        return 'Low'
    elif fri < 0.6:
        return 'Moderate'
    elif fri < 0.8:
        return 'High'
    else:
        return 'Very High'

# Apply classification
data['Risk Category'] = data['FRI'].apply(classify_risk)

# Save the processed data to a new Excel file
output_path = 'Flood_Risk_Assessment_Results.xlsx'
data.to_excel(output_path, index=False)

# Output the path to the new file
print(f"Processed data saved to {output_path}")
