import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before clustering
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Function to calculate K-means clustering and plot the Elbow curve
def plot_elbow_curve(data, max_clusters):
    distortions = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        distortions.append(kmeans.inertia_)  # Inertia measures within-cluster variance

    plt.plot(range(1, max_clusters + 1), distortions, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Distortion')
    plt.title('Elbow Method')
    plt.show()

# Set the maximum number of clusters to consider
max_clusters = 100

# Plot the Elbow curve
plot_elbow_curve(numeric_data, max_clusters)
