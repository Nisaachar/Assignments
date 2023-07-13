data("agaricus-lepiota.data")

library(arules)

# Set the minimum support threshold
min_support <- 0.85

# Convert the dataset to transactions
transactions <- as(agaricus-lepiota.data, "transactions")

# Generate frequent item sets using apriori
frequent_itemsets <- apriori(
  data = transactions,
  parameter = list(
    supp = min_support,
    maxlen = 5
  ),
  control = list(verbose = FALSE)
)

# Save frequent item sets to a file
write(frequent_itemsets, file = "frequent_0.85.output")
