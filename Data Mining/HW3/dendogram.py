import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before clustering
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Perform complete-link hierarchical clustering
linked = linkage(numeric_data, method='complete')

# Plot the dendrogram
plt.figure(figsize=(10, 6))
dendrogram(linked, orientation='top', labels=trans_data.index, distance_sort='descending', show_leaf_counts=True)
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.title('Complete-Link Hierarchical Clustering Dendrogram')
plt.show()
