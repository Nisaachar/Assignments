## Code to run the decision tree on the Party dataset ##

# Implemented by Stephen Marsland 
# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.


import dtree
import numpy as np



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



##class

## Code to implement the decision tree  ##

# Implemented by Stephen Marsland 
# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.


import numpy as np

class dtree:
	""" A basic Decision Tree"""
	
	def __init__(self):
		""" Constructor """

	def read_data(self,filename):
		fid = open(filename,"r")
		data = []
		d = []
		for line in fid.readlines():
			d.append(line.strip())
		for d1 in d:
			data.append(d1.split(","))
		fid.close()

		self.featureNames = data[0]
		self.featureNames = self.featureNames[:-1]
		data = data[1:]
		self.classes = []
		for d in range(len(data)):
			self.classes.append(data[d][-1])
			data[d] = data[d][:-1]

		return data,self.classes,self.featureNames

	def classify(self,tree,datapoint):

		if type(tree) == type("string"):
			# Have reached a leaf
			return tree
		else:
			a = list(tree.keys())[0]
			for i in range(len(self.featureNames)):
				if self.featureNames[i]==a:
					break
			
			try:
				t = tree[a][datapoint[i]]
				return self.classify(t,datapoint)
			except:
				return None

	def classifyAll(self,tree,data):
		results = []
		for i in range(len(data)):
			results.append(self.classify(tree,data[i]))
		return results

	def make_tree(self,data,classes,featureNames,maxlevel=-1,level=0,forest=0):
		""" The main function, which recursively constructs the tree"""

		nData = len(data)
		nFeatures = len(data[0])
		
		try: 
			self.featureNames
		except:
			self.featureNames = featureNames
			
		# List the possible classes
		newClasses = []
		for aclass in classes:
			if newClasses.count(aclass)==0:
				newClasses.append(aclass)

		# Compute the default class (and total entropy)
		frequency = np.zeros(len(newClasses))

		totalEntropy = 0
		index = 0
		for aclass in newClasses:
			frequency[index] = classes.count(aclass)
			totalEntropy += self.calc_entropy(float(frequency[index])/nData)

			index += 1

		default = classes[np.argmax(frequency)]

		if nData==0 or nFeatures == 0 or (maxlevel>=0 and level>maxlevel):
			# Have reached an empty branch
			return default
		elif classes.count(classes[0]) == nData:
			# Only 1 class remains
			return classes[0]
		else:

			# Choose which feature is best	
			# gain = np.zeros(nFeatures)
			# featureSet = range(nFeatures)
			# if forest != 0:
			# 	np.random.shuffle(featureSet)
			# 	featureSet = featureSet[0:forest]
			# for feature in featureSet:
			# 	g = self.calc_info_gain(data,classes,feature)
			# 	gain[feature] = totalEntropy - g

			# bestFeature = np.argmax(gain)
			# tree = {featureNames[bestFeature]:{}}
			gain = np.zeros(nFeatures)
			featureSet = list(range(nFeatures))
			for feature in featureSet:
				g = self.calc_info_gain(data, classes, feature)
				gain[feature] = g

			bestFeature = np.argmax(gain)
			tree = {featureNames[bestFeature]: {}}

			# List the values that bestFeature can take
			values = []
			for datapoint in data:
				if datapoint[feature] not in values:
					values.append(datapoint[bestFeature])

			for value in values:
				# Find the datapoints with each feature value
				newData = []
				newClasses = []
				index = 0
				for datapoint in data:
					if datapoint[bestFeature]==value:
						if bestFeature==0:
							newdatapoint = datapoint[1:]
							newNames = featureNames[1:]
						elif bestFeature==nFeatures:
							newdatapoint = datapoint[:-1]
							newNames = featureNames[:-1]
						else:
							newdatapoint = datapoint[:bestFeature]
							newdatapoint.extend(datapoint[bestFeature+1:])
							newNames = featureNames[:bestFeature]
							newNames.extend(featureNames[bestFeature+1:])
						newData.append(newdatapoint)
						newClasses.append(classes[index])
					index += 1

				# Now recurse to the next level	
				subtree = self.make_tree(newData,newClasses,newNames,maxlevel,level+1,forest)

				# And on returning, add the subtree on to the tree
				tree[featureNames[bestFeature]][value] = subtree

			return tree

	def printTree(self,tree,name):
		if type(tree) == dict:
			print(f'{name}{list(tree.keys())[0]}')

			for item in list(tree.values())[0].keys():
				print(f'{name}{item}')
				self.printTree(list(tree.values())[0][item], name + "\t")
		else:
			print(f'{name}"\t->\t"{tree}')

	def calc_entropy(self,p):
		if p!=0:
			return -p * np.log2(p)
		else:
			return 0

	# def calc_info_gain(self,data,classes,feature):

	# 	# Calculates the information gain based on entropy impurity
	# 	gain = 0
	# 	nData = len(data)

	# 	# List the values that feature can take

	# 	values = []
	# 	for datapoint in data:
	# 		if datapoint[feature] not in values:
	# 			values.append(datapoint[feature])

	# 	featureCounts = np.zeros(len(values))
	# 	entropy = np.zeros(len(values))
	# 	valueIndex = 0
	# 	# Find where those values appear in data[feature] and the corresponding class
	# 	for value in values:
	# 		dataIndex = 0
	# 		newClasses = []
	# 		for datapoint in data:
	# 			if datapoint[feature]==value:
	# 				featureCounts[valueIndex]+=1
	# 				newClasses.append(classes[dataIndex])
	# 			dataIndex += 1

	# 		# Get the values in newClasses
	# 		classValues = []
	# 		for aclass in newClasses:
	# 			if classValues.count(aclass)==0:
	# 				classValues.append(aclass)

	# 		classCounts = np.zeros(len(classValues))
	# 		classIndex = 0
	# 		for classValue in classValues:
	# 			for aclass in newClasses:
	# 				if aclass == classValue:
	# 					classCounts[classIndex]+=1 
	# 			classIndex += 1
			
	# 		for classIndex in range(len(classValues)):
	# 			entropy[valueIndex] += self.calc_entropy(float(classCounts[classIndex])/np.sum(classCounts))

	# 		# Computes the entropy gain
	# 		gain = gain + float(featureCounts[valueIndex])/nData * entropy[valueIndex]
	# 		valueIndex += 1
	# 	return gain	

	def calc_info_gain(self, data, classes, feature):
        # Calculates the information gain based on Gini index
		gini_gain = 0
		nData = len(data)

        # List the values that feature can take
		values = np.unique([datapoint[feature] for datapoint in data])

		for value in values:
			value_indices = [i for i, datapoint in enumerate(data) if datapoint[feature] == value]
			value_classes = [classes[i] for i in value_indices]

			# Calculate Gini index for the current value
			gini_value = 1.0
			unique_classes = np.unique(value_classes)
			for cls in unique_classes:
				p_i = np.sum([1 for c in value_classes if c == cls]) / len(value_classes)
				gini_value -= p_i**2

			gini_gain += (len(value_classes) / nData) * gini_value

		return gini_gain
			
