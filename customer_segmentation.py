print("Program started...")

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load the dataset (CORRECT FILE NAME)
data = pd.read_csv("Mall_Customers.csv")
print("Dataset loaded successfully")
print(data.head())

# Select features for clustering
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Visualize original data
plt.scatter(
    X['Annual Income (k$)'],
    X['Spending Score (1-100)'],
    s=50
)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Distribution')
plt.show()

# Elbow Method to find optimal clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# Apply K-Means (choose 5 clusters)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X)

# Add cluster labels to dataset
data['Cluster'] = clusters
print("\nCustomer data with cluster labels:")
print(data.head())

# Visualize clusters
plt.figure(figsize=(8,6))
sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    data=data,
    palette='Set1',
    s=100
)
plt.title('Customer Segmentation using K-Means')
plt.show()

# Save clustered data
data.to_csv("customer_clusters.csv", index=False)
print("\nClustered data saved as customer_clusters.csv")

input("Press Enter to exit...")
