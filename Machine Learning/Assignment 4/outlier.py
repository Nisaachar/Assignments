import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Example arrays of points for three different clusters
coordinatesA = [(-0.392, -1.258, -0.066), (-0.251, -1.781, -1.495), (-0.736, -1.694, -0.686), (-0.288, -2.116, -1.165), (-0.597, -1.577, -0.618)]
coordinatesB = [(0.917, -0.961, 0.055), (1.204, -0.605, 0.351), (0.778, -0.436, -0.220), (1.075, -1.199, -0.141), (1.280, -1.188, 0.053)]
coordinatesC = [(-0.823, -0.042, 1.254), (-0.854, -0.654, 0.771), (-1.027, -0.269, 0.893), (-1.113, -0.271, 0.930), (-0.849, -0.430, 0.612)]

# Define initial medians for each cluster
medianA = (-0.4528, -1.6852, -0.926)
medianB = (-1.0508, -0.8778, 0.0196)
medianC = (-0.9332, -0.3332, 0.892)

# Function to find outliers based on Euclidean distance
def find_outlier_coordinate(coordinates, median):
    max_distance = float('-inf')
    outlier_coord = None

    for coord in coordinates:
        distance = euclidean_distance(coord, median)
        if distance > max_distance:
            max_distance = distance
            outlier_coord = coord

    return outlier_coord, max_distance

# Find outlier coordinate for each cluster
outlier_coord_A, max_distance_A = find_outlier_coordinate(coordinatesA, medianA)
outlier_coord_B, max_distance_B = find_outlier_coordinate(coordinatesB, medianB)
outlier_coord_C, max_distance_C = find_outlier_coordinate(coordinatesC, medianC)

# Output the outlier coordinate and its distance for each cluster
print(f"Outlier Coordinate for Cluster A: {outlier_coord_A} with distance: {max_distance_A}")
print(f"Outlier Coordinate for Cluster B: {outlier_coord_B} with distance: {max_distance_B}")
print(f"Outlier Coordinate for Cluster C: {outlier_coord_C} with distance: {max_distance_C}")
