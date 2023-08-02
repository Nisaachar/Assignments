#P4.

#1
# Load the required libraries
library(dbscan)

# Load the iris dataset
data(iris)

# Remove the "Species" column
iris_features <- iris[, -5]  # Exclude the 5th column ("Species")

# Compute the local outlier factor using dbscan
lof_values <- lof(iris_features)

# Add the LOF values to the original iris dataset
iris$LOF <- lof_values

# View the LOF values for each object
print(iris$LOF)


#2
sorted_iris <- iris[order(-iris$LOF), ]

# Get the top 5 outliers
top_5_outliers <- head(sorted_iris, 5)

# Print the top 5 outliers
print(top_5_outliers)


#3
lof_density <- density(iris$LOF)

print(lof_density)

# Generate the plot diagram for LOF density
plot(lof_density, main = "Kernel Density Estimate of LOF Values",
     xlab = "Local Outlier Factor (LOF)", ylab = "Density")







