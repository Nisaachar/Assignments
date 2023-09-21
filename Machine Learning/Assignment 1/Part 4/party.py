## Code to run the decision tree on the Party dataset ##

# Implemented by Stephen Marsland 
# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.


import dtree
import numpy as np



tree = dtree.dtree()
party,classes,features = tree.read_data('party.data')
t=tree.make_tree(party,classes,features)
# tree.printTree(t,' ')

# print(tree.classifyAll(t,party))

# for i in range(len(party)):
#     tree.classify(t,party[i])

# print("True Classes")
# print(classes)

true_classes = classes
predicted_classes = tree.classifyAll(t, party)

# Print true and predicted class labels for each instance
print("Instance\tTrue Class\tPredicted Class")
for i in range(len(party)):
    print(f"{party[i]}\t{true_classes[i]}\t\t{predicted_classes[i]}")

# Calculate training error rate
error_count = sum(1 for true_class, predicted_class in zip(true_classes, predicted_classes) if true_class != predicted_class)
training_error_rate = error_count / len(true_classes)

print("\nTraining Error Rate:", training_error_rate)

