import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
bedrooms = np.array([1, 1, 2, 2, 3, 3,  4, 4, 5, 5, 5])
house_price = np.array([15000, 18000, 27000, 34000, 34000, 50000, 68000, 65000, 81000, 85000, 90000])

# Mengubah bentuk data agar sesuai dengan input model Linear Regression
bedrooms = bedrooms.reshape(-1, 1)

# Membuat model Linear Regression
model = LinearRegression()

# Melatih model dengan data
model.fit(bedrooms, house_price)

# Membuat prediksi menggunakan model
predictions = model.predict(bedrooms)

# Plot hasil model
plt.scatter(bedrooms, house_price, color='blue', label='Data Asli')
plt.plot(bedrooms, predictions, color='red', linewidth=2, label='Model Linear Regression')
plt.xlabel('Jumlah Bedrooms')
plt.ylabel('Harga Rumah')
plt.title('Linear Regression untuk Prediksi Harga Rumah')
plt.legend()
plt.show()

# Menampilkan koefisien dan intercept dari model
print("Koefisien (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
