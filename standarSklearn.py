from sklearn import preprocessing

# Original data
data = [[12000000, 33], [35000000, 45], [4000000, 23], [6500000, 26], [9000000, 29]]

# Fit a StandardScaler to the data and transform it
scaler = preprocessing.StandardScaler().fit(data)
scaled_data = scaler.transform(data)

# Print the scaled data
print(scaled_data)