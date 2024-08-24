import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data_path = 'lat_long_drainage_mindist.csv'
data = pd.read_csv(data_path)

# Plot histogram for Elevation
plt.figure(figsize=(10, 5))
plt.hist(data['Elevation'], bins=30, color='blue', alpha=0.7)
plt.title('Histogram of Elevation')
plt.xlabel('Elevation')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot histogram for Minimum Distance to Drainage
plt.figure(figsize=(10, 5))
plt.hist(data['Nearest_Drainage_Distance'], bins=30, color='green', alpha=0.7)
plt.title('Histogram of Minimum Distance to Drainage')
plt.xlabel('Minimum Distance (mindist)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
