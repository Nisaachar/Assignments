import math

def euclidean_distance(point1, point2):
    # Ensure both points have three coordinates
    if len(point1) != 3 or len(point2) != 3:
        raise ValueError("Points should have three coordinates (x, y, z)")

    # Unpack coordinates
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calculate Euclidean distance
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance

def sum_of_squares(centroid, points):
    sum_squares = 0
    distances = []
    for i, point in enumerate(points):
        distance = euclidean_distance(centroid, point)
        distances.append(distance)
        sum_squares += distance ** 2
        print(f"Distance between Centroid {centroid} and point {i + 1} {point} in this Cluster: {distance}")
    return sum_squares, distances

# Example centroids
CentroidA = (-0.4528, -1.6852, -0.926)
centroidB = (-1.0508, -0.8778, 0.0196)
centroidC = (-0.9332, -0.3332, 0.892)

# Example arrays of points for three different clusters
coordinatesA = [(-0.392, -1.258, -0.066), (-0.251, -1.781, -1.495), (-0.736, -1.694, -0.686), (-0.288, -2.116, -1.165), (-0.597, -1.577, -0.618)]
coordinatesB = [(0.917, -0.961, 0.055), (1.204, -0.605, 0.351), (0.778, -0.436, -0.220), (1.075, -1.199, -0.141), (1.280, -1.188, 0.053)]
coordinatesC = [(-0.823, -0.042, 1.254), (-0.854, -0.654, 0.771), (-1.027, -0.269, 0.893), (-1.113, -0.271, 0.930), (-0.849, -0.430, 0.612)]

# Calculate sum of squares and distances for each cluster
sum_squares_A, distances_A = sum_of_squares(CentroidA, coordinatesA)
sum_squares_B, distances_B = sum_of_squares(centroidB, coordinatesB)
sum_squares_C, distances_C = sum_of_squares(centroidC, coordinatesC)

# Display sum of squares for each cluster
print(f"\nSum of squares for Cluster 1: {sum_squares_A}")
print(f"Sum of squares for Cluster 2: {sum_squares_B}")
print(f"Sum of squares for Cluster 3: {sum_squares_C}")
