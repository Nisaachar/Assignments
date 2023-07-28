import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before clustering
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Function to calculate K-means clustering and compute the average Silhouette score
def get_silhouette_scores(data, max_clusters):
    silhouette_scores = []
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        labels = kmeans.labels_
        silhouette_scores.append(silhouette_score(data, labels))

    return silhouette_scores

# Set the maximum number of clusters to consider
max_clusters = 10

# Get Silhouette scores
silhouette_scores = get_silhouette_scores(numeric_data, max_clusters)

# Plot Silhouette scores
plt.plot(range(2, max_clusters + 1), silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method')
plt.show()

# Find the optimal number of clusters based on Silhouette scores
optimal_k = np.argmax(silhouette_scores) + 2  # Add 2 because we started from k=2
print("Optimal number of clusters (k) based on Silhouette method:", optimal_k)
