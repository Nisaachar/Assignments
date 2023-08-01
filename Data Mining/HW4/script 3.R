# Load the iris dataset
data(iris)

# Remove the "Species" column
iris_features <- iris[, 1:4]

# Set the number of clusters (k) to 3
k <- 3

# Perform k-means clustering
kmeans_result <- kmeans(iris_features, centers = k, nstart = 25)

# Get the cluster assignments for each data point
cluster_assignments <- kmeans_result$cluster

# Find the data points that are not assigned to any clusters (outliers)
outliers <- which(is.na(cluster_assignments))

# Print the indices of the outlier data points
cat("Indices of outlier data points:", outliers, "\n")

# Print the outlier data points themselves
outlier_data <- iris[outliers, ]
print(outlier_data)

#2
centroids <- kmeans_result$centers

# Display the centroids
print("Centroids of each cluster:")
print(centroids)



#3
distances <- sqrt(rowSums((t(iris_features) - t(centroids[kmeans_result$cluster, ]))^2))

# Reshape the distances into a data frame for better visualization
distances_df <- matrix(distances, nrow = nrow(iris_features), ncol = k, byrow = TRUE)
colnames(distances_df) <- paste0("Distance_to_Centroid_", 1:k)

# Add the distances data frame to the original iris data
iris_with_distances <- cbind(iris, distances_df)

# Display the distances for the first 10 data points (you can view more or all data points)
print("Distances between objects and cluster centroids:")
print(iris_with_distances[1:10, ])



#4

data(iris)

# Remove the "Species" column
iris_features <- iris[, 1:4]

# Function to calculate LOF for each data point
calculate_lof <- function(data, k) {
  distances <- as.matrix(dist(data))
  n <- nrow(data)
  lof_values <- rep(0, n)
  
  for (i in 1:n) {
    k_distances <- sort(distances[i, distances[i, ] > 0])[1:k]
    neighbors <- order(distances[i, ])[2:(k + 1)]
    reachability_distances <- pmax(k_distances, distances[neighbors, i])
    local_reachability_density <- 1 / mean(reachability_distances)
    lof_values[i] <- mean(local_reachability_density / (1 / k_distances))
  }
  
  return(lof_values)
}

# Set the number of nearest neighbors (k) for LOF calculation
k <- 5

# Compute the Local Outlier Factor (LOF) for each data point
lof_values <- calculate_lof(iris_features, k)

# Combine the LOF values with the original iris data
iris_with_lof <- cbind(iris, LOF = lof_values)

# Display the LOF values for the first 10 data points (you can view more or all data points)
print("Local Outlier Factor (LOF) values:")
print(iris_with_lof[1:10, ])


#5
# Load the required library
library(dbscan)

# Load the iris dataset
data(iris)

# Remove the "Species" column
iris_features <- iris[, 1:4]

# Compute the density-based clustering using dbscan
dbscan_result <- dbscan(iris_features, eps = 0.5, minPts = 5)

# Get the indices of the outliers (noise points) as identified by dbscan
outlier_indices <- which(dbscan_result$cluster == 0)

# Extract the outlier data points from the original iris dataset
outliers <- iris[outlier_indices, ]

# Display the top 5 outliers
print("Top 5 outliers:")
print(outliers[1:5, ])


#6
# Load the required libraries
# Load the required libraries
library(ggplot2)
library(dbscan)

# Load the iris dataset
data(iris)

# Remove the "Species" column
iris_features <- iris[, c("Petal.Length", "Petal.Width")]

# Compute the density-based clustering using dbscan
dbscan_result <- dbscan(iris_features, eps = 0.5, minPts = 5)

# Get the indices of the outliers (noise points) as identified by dbscan
outlier_indices <- which(dbscan_result$cluster == 0)

# Extract the outlier data points from the original iris dataset
outliers <- iris[outlier_indices, ]

# Add cluster and outlier information to the iris dataset
iris$Cluster <- dbscan_result$cluster
iris$IsOutlier <- ifelse(1:nrow(iris) %in% outlier_indices, "Outlier", "Inlier")

# Create a new data frame for centroids with appropriate column names
centroid_data <- data.frame(Petal.Length = dbscan_result$centers[, 1], Petal.Width = dbscan_result$centers[, 2])

# Create the plot
ggplot(iris, aes(x = "Petal.Length", y = "Petal.Width", color = factor(Cluster), shape = IsOutlier)) +
  geom_point(size = 4) +
  geom_point(data = centroid_data, aes(x = "Petal.Length", y = "Petal.Width"), color = "black", size = 5, shape = 2) +
  scale_color_discrete(name = "Cluster") +
  scale_shape_manual(name = "Outlier", values = c(16, 17)) +
  theme_minimal()




