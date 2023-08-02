# Set a seed for reproducibility
set.seed(42)

# (1) Generate 200 normally distributed random numbers
random_numbers <- rnorm(200)

print(random_numbers)

# (2) Show the summary of the numbers using min, Q1, Median, Mean, Q3, and Max
summary_stats <- summary(random_numbers)
print(summary_stats)

# (3) Draw the boxplot of this data
boxplot(random_numbers, main = "Boxplot of Random Numbers")

# (4) Report the values of data points which lie beyond the extremes of the whiskers
# Calculate the interquartile range (IQR)
Q1 <- quantile(random_numbers, 0.25)
Q3 <- quantile(random_numbers, 0.75)
IQR <- Q3 - Q1

# Calculate the lower and upper bounds of the whiskers
lower_whisker <- Q1 - 1.5 * IQR
upper_whisker <- Q3 + 1.5 * IQR

# Identify the outliers
outliers <- random_numbers[random_numbers < lower_whisker | random_numbers > upper_whisker]

# Report the values of outliers
print("Outliers:")
print(outliers)


