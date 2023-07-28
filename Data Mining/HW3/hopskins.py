import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Load the trans_data dataset
trans_data = pd.read_csv('trans_data.csv')

# Remove the categorical attributes 'Channel' and 'Region' before computing the Hopkins statistic
numeric_data = trans_data.drop(columns=['Channel', 'Region'])

# Function to generate uniform random data with the same range as the numeric data
def random_data_generator(data):
    return np.random.rand(len(data), len(data[0])) * (data.max() - data.min()) + data.min()

# Compute the Hopkins statistic
def hopkins_statistic(data, n_samples=100):
    data = data.values.T  # Transpose the data to match the dimension
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='brute').fit(data)
    
    rand_data = random_data_generator(data)
    rand_nbrs = NearestNeighbors(n_neighbors=1, algorithm='brute').fit(rand_data)

    u_distances, _ = nbrs.kneighbors(data, n_neighbors=2)
    r_distances, _ = rand_nbrs.kneighbors(rand_data, n_neighbors=1)

    hopkins_stat = np.sum(u_distances) / (np.sum(u_distances) + np.sum(r_distances))
    return hopkins_stat

hopkins_statistic_value = hopkins_statistic(numeric_data)
print("Hopkins Statistic:", hopkins_statistic_value)
