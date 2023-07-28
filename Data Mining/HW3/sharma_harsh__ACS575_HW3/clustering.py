import pandas as pd
from sklearn.cluster import KMeans

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before clustering
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Perform k-means clustering with k=6
kmeans = KMeans(n_clusters=6, random_state=42)
cluster_labels = kmeans.fit_predict(numeric_data)

# Add cluster labels to the original DataFrame
trans_data['Cluster'] = ["Cluster" + str(label + 1) for label in cluster_labels]

# Save the result to a new CSV file "k-means-result.csv"
trans_data.to_csv('k-means-result.csv', index=False)

# Display the first few rows of the result DataFrame
print(trans_data.head())
