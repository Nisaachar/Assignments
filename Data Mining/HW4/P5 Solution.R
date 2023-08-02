# Load the required library
library(datasets)

# Load the iris dataset
data(iris)

# Remove the "Species" column
iris_features <- iris[, -5]  # Exclude the 5th column ("Species")

# Compute the distance matrix using dist() function with k=1
distance_matrix <- as.matrix(dist(iris_features, method = "euclidean"))

# Set the diagonal elements to a large value to exclude the distance to itself
diag(distance_matrix) <- Inf

# Find the minimum distance to the nearest neighbor for each data object
nearest_neighbor_distance <- apply(distance_matrix, 1, min)

# Print the distance to the nearest neighbor for each data object
print(nearest_neighbor_distance)



#2
top_5_outliers_indices <- order(nearest_neighbor_distance, decreasing = TRUE)[1:5]
top_5_outliers <- iris[top_5_outliers_indices, ]

# Print the data objects with the top 5 largest distances as outliers
print("Top 5 Outliers:")
print(top_5_outliers)



#3
k_nearest_neighbors <- 3
distance_matrix <- as.matrix(dist(iris_features, method = "euclidean"))

# Set the diagonal elements to a large value to exclude the distance to itself
diag(distance_matrix) <- Inf

# Find the k-nearest neighbors for each data object
k_nearest_distances <- apply(distance_matrix, 1, function(x) sort(x)[1:k_nearest_neighbors])

# Print the distances to the k-nearest neighbors for each data object
print(k_nearest_distances)



#4
top_5_outliers_indices <- order(apply(k_nearest_distances, 1, max), decreasing = TRUE)[1:5]
top_5_outliers <- iris[top_5_outliers_indices, ]

# Print the data objects with the top 5 largest distances as outliers
print("Top 5 Outliers:")
print(top_5_outliers)



#5

# Compute the distance matrix using dist() function with k=1
distance_matrix_k1 <- as.matrix(dist(iris_features, method = "euclidean"))

# Set the diagonal elements to a large value to exclude the distance to itself
diag(distance_matrix_k1) <- Inf

# Find the nearest neighbor distance for each data object with k=1
nearest_neighbor_distance_k1 <- apply(distance_matrix_k1, 1, min)

# (2) Report the data objects with top 5 largest distances as outliers for k=1
top_5_outliers_indices_k1 <- order(nearest_neighbor_distance_k1, decreasing = TRUE)[1:5]
outliers_k1 <- iris[top_5_outliers_indices_k1, ]

# Compute the distance matrix using dist() function with k=3
k_nearest_neighbors <- 3
distance_matrix_k3 <- as.matrix(dist(iris_features, method = "euclidean"))

# Set the diagonal elements to a large value to exclude the distance to itself
diag(distance_matrix_k3) <- Inf

# Find the k-nearest neighbors for each data object with k=3
k_nearest_distances <- apply(distance_matrix_k3, 1, function(x) sort(x)[1:k_nearest_neighbors])

# (4) Report the data objects with top 5 largest distances as outliers for k=3
top_5_outliers_indices_k3 <- order(apply(k_nearest_distances, 1, max), decreasing = TRUE)[1:5]
outliers_k3 <- iris[top_5_outliers_indices_k3, ]

# (5) List the data objects that appear in both lists from (2) and (4) as outliers
common_outliers <- intersect(outliers_k1$Row.names, outliers_k3$Row.names)
if (length(common_outliers) > 0) {
  print("Data objects appearing in both lists as outliers:")
  print(iris[common_outliers, ])
} else {
  print("No data objects found in both lists as outliers.")
}



#(6) Count the number of neighboring objects per each object within a distance threshold of 2
neighbor_distance_threshold <- 2
neighboring_objects_count <- apply(distance_matrix, 1, function(x) sum(x <= neighbor_distance_threshold))

# Print the count of neighboring objects within the distance threshold for each data object
print(neighboring_objects_count)



#(7) Report the data objects with top 5 smallest neighbors as outliers
top_5_outliers_indices <- order(neighboring_objects_count, decreasing = FALSE)[1:5]
top_5_outliers <- iris[top_5_outliers_indices, ]

# Print the data objects with the top 5 smallest neighbors as outliers
print("Top 5 Outliers:")
print(top_5_outliers)






