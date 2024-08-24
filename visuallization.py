import pandas as pd
from simpledbf import Dbf5
import matplotlib.pyplot as plt
import numpy as np

# Read DBF file
dbf = Dbf5('Surat Images/Surat (Tapi basin)/Results/Results/Statistics/Surat_Validation_2006_Flood_2D_2007CSBaseDefault_2D_Flood_statistics_elements_0.dbf')
df = dbf.to_dataframe()

# Print the first few rows and the shape of the DataFrame
print(df.head())
print(df.shape)

# Save as CSV (uncomment if needed)
# df.to_csv('yourfile.csv', index=False)

# Assuming you want to plot the first column against an index
column_name = df.columns[0]  # Replace with the actual column name if known
x = np.linspace(1, df.shape[0], df.shape[0])

# Check a specific value in the x array
print(x[4])

# Plot the data
plt.plot(x, df[column_name])
plt.xlabel('Index')
plt.ylabel(column_name)
plt.title('Plot of {} vs Index'.format(column_name))
plt.show()
