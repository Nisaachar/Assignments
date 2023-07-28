# Load the dataset from .data file
data <- read.table("arrhythmia.data", header = FALSE, sep = ",")


library(dplyr)

numeric_data <- select_if(data, is.numeric)

normalized_data <- as.data.frame(scale(numeric_data))


normalized_data[1:10,]

num_bins <- 10
bin_names <- paste(names(numeric_data), rep("Bin", num_bins), 1:num_bins, sep = "_")

discretized_data <- lapply(numeric_data, function(x) cut(x, breaks = num_bins, labels = FALSE, include.lowest = TRUE))

discretized_data <- lapply(discretized_data, function(x) {
  x <- as.integer(x)
  x[!is.na(x)] <- bin_names[x[!is.na(x)]]
  x
})

discretized_data <- as.data.frame(discretized_data)

data[, names(numeric_data)] <- discretized_data

data[1:2,]
