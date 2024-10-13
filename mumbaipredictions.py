import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
output_dir = 'surat_flood_data'

# Read each CSV file
elevation_df = pd.read_csv(f'{output_dir}/elevation.csv')
rainfall_df = pd.read_csv(f'{output_dir}/rainfall.csv')
distance_df = pd.read_csv(f'{output_dir}/distance_from_sea.csv')
risk_df = pd.read_csv(f'{output_dir}/risk_of_flood.csv')

# Merge dataframes on Latitude and Longitude
combined_df = pd.merge(elevation_df, rainfall_df, on=['Latitude', 'Longitude'])
combined_df = pd.merge(combined_df, distance_df, on=['Latitude', 'Longitude'])
combined_df = pd.merge(combined_df, risk_df, on=['Latitude', 'Longitude'])

# Separate features and target
X = combined_df.drop('Risk_of_Flood', axis=1)  # Features
y = combined_df['Risk_of_Flood']  # Target

# Split into train and test sets
# Train a Decision Tree Classifier
# Train a Random Forest Classifier
forest_model = RandomForestClassifier(random_state=42, n_estimators=100)
forest_model.fit(X, y)
mumbai_data_loaded = pd.read_csv('mumbai_data.csv')

# Step 6: Use the trained Random Forest model to predict flood risk
predictions = forest_model.predict(mumbai_data_loaded)

# Add predictions to the Mumbai dataset
mumbai_data_loaded['Predicted Flood Risk'] = predictions

# Step 7: Save the predictions to a new CSV file
mumbai_data_loaded.to_csv('mumbai_data_with_predictions.csv', index=False)

# Print the first few rows of the predictions
# print(mumbai_data_loaded)
# Count the frequency of each predicted flood risk zone
flood_risk_counts = mumbai_data_loaded['Predicted Flood Risk'].value_counts()

# Display the frequencies of each type of flood risk zone
print("Frequency of each predicted flood risk zone:")
print(flood_risk_counts)
