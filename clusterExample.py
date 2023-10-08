import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data (contoh data)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Frequency': [5, 1, 10, 3, 8, 2, 6, 9, 4, 7],  # Frekuensi Pembelian
    'Monetary': [300, 50, 700, 150, 600, 80, 400, 900, 200, 650]  # Total Pengeluaran
}

df = pd.DataFrame(data)

# Menggunakan hanya kolom 'Frequency' dan 'Monetary' untuk segmentasi
X = df[['Frequency', 'Monetary']]

# Normalisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Menentukan jumlah cluster (k) dengan metode Elbow
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method untuk menentukan jumlah cluster yang optimal
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('Elbow Method')
plt.show()

# Dari grafik, pilih jumlah cluster yang optimal (misalnya, 3)
num_clusters = 3

# Melakukan K-Means dengan jumlah cluster yang telah dipilih
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Menambahkan label cluster ke DataFrame
df['Cluster'] = cluster_labels

# Menampilkan hasil segmentasi pelanggan
print(df)
