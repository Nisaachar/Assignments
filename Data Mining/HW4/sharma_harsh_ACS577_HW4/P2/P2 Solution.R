# Set a seed for reproducibility
set.seed(42)

# (1) Generate 200 normally distributed random numbers for attribute x
x <- rnorm(200)

# (2) Generate 200 normally distributed random numbers for attribute y
y <- rnorm(200)

# (3) Combine x and y to create a 2-dimensional dataset
data_2d <- data.frame(x, y)

# (4) Display the first 5 rows of the dataset
print(head(data_2d))

# (5) Calculate the lower and upper bounds of the whiskers for attribute x
Q1_x <- quantile(x, 0.25)
Q3_x <- quantile(x, 0.75)
IQR_x <- Q3_x - Q1_x
lower_whisker_x <- Q1_x - 1.5 * IQR_x
upper_whisker_x <- Q3_x + 1.5 * IQR_x

# Calculate the lower and upper bounds of the whiskers for attribute y
Q1_y <- quantile(y, 0.25)
Q3_y <- quantile(y, 0.75)
IQR_y <- Q3_y - Q1_y
lower_whisker_y <- Q1_y - 1.5 * IQR_y
upper_whisker_y <- Q3_y + 1.5 * IQR_y

# (2) List the values of any data points which lie beyond the extremes of the whiskers in the boxplot of x
outliers_x <- x[x < lower_whisker_x | x > upper_whisker_x]
print("Outliers in x:")
print(outliers_x)

# (3) List the values of any data points which lie beyond the extremes of the whiskers in the boxplot of y
outliers_y <- y[y < lower_whisker_y | y > upper_whisker_y]
print("Outliers in y:")
print(outliers_y)

# (4) Report the values of outliers in both x and y
outliers_both <- data_2d[data_2d$x %in% outliers_x & data_2d$y %in% outliers_y, ]
print("Outliers in both x and y:")
print(outliers_both)

# (5) Draw a 2-dimensional boxplot with the input data and mark the outlier data with "orange" color
boxplot(x, y, col = ifelse(data_2d$x %in% outliers_x & data_2d$y %in% outliers_y, "orange", "blue"),
        main = "2-Dimensional Boxplot with Outliers Marked",
        xlab = "Attribute x", ylab = "Attribute y")
