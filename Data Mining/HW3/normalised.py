import pandas as pd

# Load the original dataset
data = pd.read_csv('original_data.csv')

# Select the numeric attributes for standardization
numeric_attributes = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

# Calculate the mean and standard deviation of each numeric attribute
means = data[numeric_attributes].mean()
stds = data[numeric_attributes].std()

# Standardize the numeric attributes using z-score normalization
standardized_data = (data[numeric_attributes] - means) / stds

# Combine the standardized attributes with the categorical attributes CHANNEL and REGION
trans_data = pd.concat([data[['Channel', 'Region']], standardized_data], axis=1)

# Save the standardized data to a new CSV file named "trans_data.csv"
trans_data.to_csv('trans_data.csv', index=False)