## Code to run the decision tree on the Party dataset ##

# Implemented by Stephen Marsland 
# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.


import dtree
import numpy as np


def bootstrap_split(data, percentage=0.8):
    """Split the data into training and validation sets using bootstrap."""
    num_samples = len(data)
    train_size = int(percentage * num_samples)
    
    # Generate a bootstrap sample
    indices = np.random.choice(range(num_samples), size=train_size, replace=True)
    train_data = [data[i] for i in indices]

    # Validation set is the remaining data not included in the training set
    validation_data = [data[i] for i in range(num_samples) if i not in indices]
    
    return train_data, validation_data


# tree = dtree.dtree()
# party,classes,features = tree.read_data('party.data')
# t=tree.make_tree(party,classes,features)
# # tree.printTree(t,' ')

# # print(tree.classifyAll(t,party))

# # for i in range(len(party)):
# #     tree.classify(t,party[i])

# # print("True Classes")
# # print(classes)

# true_classes = classes
# predicted_classes = tree.classifyAll(t, party)

# # Print true and predicted class labels for each instance
# print("Instance\tTrue Class\tPredicted Class")
# for i in range(len(party)):
#     print(f"{party[i]}\t{true_classes[i]}\t\t{predicted_classes[i]}")

# # Calculate training error rate
# error_count = sum(1 for true_class, predicted_class in zip(true_classes, predicted_classes) if true_class != predicted_class)
# training_error_rate = error_count / len(true_classes)

# print("\nTraining Error Rate:", training_error_rate)

tree = dtree.dtree()

# Read the data
party, classes, features = tree.read_data('party.data')

# Split the data into training and validation sets using bootstrap
training_data, validation_data = bootstrap_split(list(zip(party, classes)), percentage=0.8)
training_party, training_classes = zip(*training_data)
validation_party, validation_classes = zip(*validation_data)

# Build the decision tree model using the training set
t = tree.make_tree(list(training_party), list(training_classes), features)

# Classify instances in the validation set
true_classes = list(validation_classes)
predicted_classes = tree.classifyAll(t, list(validation_party))

# Print the count of instances in the validation set
print(f"Number of instances in the validation set: {len(validation_party)}")

# Print true and predicted class labels for each instance in the validation set
print("Validation Instance\tTrue Class\tPredicted Class")
for i in range(len(validation_party)):
    print(f"{validation_party[i]}\t{true_classes[i]}\t\t{predicted_classes[i]}")

# Calculate test error rate
error_count = sum(1 for true_class, predicted_class in zip(true_classes, predicted_classes) if true_class != predicted_class)
test_error_rate = error_count / len(true_classes)

  

print("\nTest Error Rate:", test_error_rate)

train_true_classes = list(training_classes)
train_predicted_classes = tree.classifyAll(t, list(training_party))

train_error_count = sum(1 for true_class, predicted_class in zip(train_true_classes, train_predicted_classes) if true_class != predicted_class)
train_error_rate = train_error_count / len(train_true_classes)

print("\nTraining Error Rate:", train_error_rate)



