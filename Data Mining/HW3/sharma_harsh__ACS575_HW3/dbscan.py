import pandas as pd
from sklearn.cluster import DBSCAN

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before clustering
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Perform DBSCAN clustering with ε=0.5 and minPts=15
dbscan = DBSCAN(eps=0.5, min_samples=15)
cluster_labels = dbscan.fit_predict(numeric_data)

# Add cluster labels to the original DataFrame
trans_data['Cluster'] = cluster_labels

# Save the result to a new CSV file "DBSCAN-result.csv"
trans_data.to_csv('DBSCAN-result.csv', index=False)

# Display the first few rows of the result DataFrame
print(trans_data.head())
