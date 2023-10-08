import os
import pandas as pd

# Provide the directory path
directory_path = r'D:\python'

# Provide the file name separately
file_name = 'example_data1.csv'

file_path = os.path.join(directory_path, file_name)

df = pd.read_csv(file_path, encoding='latin1')

# Assuming that 'X_data' and 'y_data' are column names in your CSV file
X_data = df['data3']
y_data = df['data4']

# Now you can perform various operations on X_data and y_data as needed.

# Example: Printing the first few rows of X_data and y_data
print("X_data:")
print(X_data.head())

print("\ny_data:")
print(y_data.head())

# Example: Checking basic statistics of X_data
print("\nBasic statistics for X_data:")
print(X_data.describe())
