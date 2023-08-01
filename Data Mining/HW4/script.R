set.seed(3147)
x <- rnorm(200)

summary(x)

#outliers
boxplot.stats(x)$out

boxplot(x)



#q2.

y <- rnorm(200)
df <- data.frame(x,y)
#rm(x,y)
head(df)

#(2)
attach(df)

(a<-which(x %in% boxplot.stats(x)$out))

outliers_values_x <- x[a]

cat("Outliers values in X:", outliers_values_x, "\n")

#for y
(b <- which(y %in% boxplot.stats(y)$out))

outliers_values_y <- x[b]

cat("Outliers values in X:", outliers_values_y, "\n")


detach(df)

#outliers in both x and y
(outliers.list1 <- intersect(outliers_values_x,outliers_values_y))

plot(df)

points(df[outliers.list1,], col="orange", pch="+", cex=2.5)


(outlier.list2 <- union(a,b))

plot(df)

points(df[outlier.list2,], col="orange", pch="x", cex=2)




#P3







#pick top 5 as outliers
outliers<- order(outlier.scores, decreasing=T)[1:5]
#who are outliers
print(outliers)

library(Rlof)

library(doParallel)
library(foreach)
library(iterators)
library(parallel)

outlier.scores <- lof(iris2, k=5)

outlier.score <- lof(iris2, k=c(5:10))


iris2 <- iris[,1:4]
kmeans.result <- kmeans(iris2, centers = 3)
kmeans.result$centers

kmeans.result$cluster

centers <- kmeans.result$centers[kmeans.result$cluster, ]
distances <- sqrt(rowSums((iris - centers)^2))

outliers <- order(distances, decreasing=T)[1:5]
print(outliers)

print(iris2[outliers,])

plot(iris2[,c("Sepal.Length", "Sepal.Width")], pch="o", col = kmeans.result$cluster, cex=0.3)

points(kmeans.result$centers[,c("Sepal.Length", "Sepal.Width")], col=1:3, pch=8, cex=1.5)

points(iris2[outliers, c("Sepal.Length", "Sepal.Width")], pch="+", col=4, cex=1.5)


#P5


f <- stl(AirPassengers, "periodic", robust=TRUE)
(outliers <- which(f$wights<1e-8))

op <- par(mar=c(0,4,0,3), oma=c(5,0,4,0), mfcol=c(4,1))

plot(f, set.pars=NULL)

sts <- f$time.series

points(time(sts)[outliers], 0.8*sts[,"remainder"][outliers], pch="x",col="red")

par(op)








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

# Generate the plot diagram for LOF density
plot(lof_density, main = "Kernel Density Estimate of LOF Values",
     xlab = "Local Outlier Factor (LOF)", ylab = "Density")




















