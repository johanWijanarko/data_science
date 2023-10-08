
import os
import pandas as pd

# Provide the directory path
directory_path = r'D:\python'

# Provide the file name separately
file_name = 'example_data1.csv'

# Combine the directory path and file name to create the full file path
file_path = os.path.join(directory_path, file_name)

# Read the CSV file from the specified path with a specific encoding (e.g., 'latin1')
df = pd.read_csv(file_path, encoding='latin1')

# Print the entire DataFrame
print(df.to_string())