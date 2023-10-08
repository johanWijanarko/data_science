# Import the MinMaxScaler class
from sklearn.preprocessing import MinMaxScaler

# Create an instance of MinMaxScaler
scaler = MinMaxScaler()

# Sample data (replace this with your own dataset)
data = [[12000000, 33], [35000000, 45], [4000000, 23], [6500000, 26], [9000000, 29]]

# Fit the scaler to your data (compute min and max values for each feature)
scaler.fit(data)

# Transform your data to scale features to the range [0, 1]
scaled_data = scaler.transform(data)

# The scaled_data variable now contains your scaled data
print("Original Data:")
print(data)
print("\nScaled Data (MinMax Scaling):")
print(scaled_data)