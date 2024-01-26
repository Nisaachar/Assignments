from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

def calculate_silhouette(coordinates, median):
    kmeans = KMeans(n_clusters=3, n_init=10)
    clusters = kmeans.fit_predict(coordinates)
    silhouette_avg = silhouette_score(coordinates, clusters)
    print(f"The silhouette score for the provided coordinates using median {median} is: {silhouette_avg}")
    return silhouette_avg

# Example arrays of points for three different clusters
coordinatesA = [(-0.392, -1.258, -0.066), (-0.251, -1.781, -1.495), (-0.736, -1.694, -0.686), (-0.288, -2.116, -1.165), (-0.597, -1.577, -0.618)]
coordinatesB = [(0.917, -0.961, 0.055), (1.204, -0.605, 0.351), (0.778, -0.436, -0.220), (1.075, -1.199, -0.141), (1.280, -1.188, 0.053)]
coordinatesC = [(-0.823, -0.042, 1.254), (-0.854, -0.654, 0.771), (-1.027, -0.269, 0.893), (-1.113, -0.271, 0.930), (-0.849, -0.430, 0.612)]

# Define medians for each cluster
medianA = (-0.4528, -1.6852, -0.926)
medianB = (-1.0508, -0.8778, 0.0196)
medianC = (-0.9332, -0.3332, 0.892)

# Calculate Silhouette Coefficient for each cluster
silhouette_score_A = calculate_silhouette(coordinatesA, medianA)
silhouette_score_B = calculate_silhouette(coordinatesB, medianB)
silhouette_score_C = calculate_silhouette(coordinatesC, medianC)
