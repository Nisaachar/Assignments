# Part II. Neural Network from Scratch

import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return max(0, x)

# Define the weights
weights = {
    'w3,1': -0.1, 'w4,1': 0.2, 'w3,2': -0.2, 'w4,2': 0.3,
    'w3,0': 0.1, 'w5,3': -0.1, 'w6,3': 0.1, 'w4,0': 0.1,
    'w5,4': 0.2, 'w6,4': -0.2, 'w5,0': 0.1, 'w6,0': 0.1
}

# Define the input values
inputs = {'Neuron 1': 0.3, 'Neuron 2': 0.6}

# Calculate the output for each neuron
z3 = weights['w3,0'] + weights['w3,1'] * inputs['Neuron 1'] + weights['w3,2'] * inputs['Neuron 2']
a3 = round(relu(z3), 2)

z4 = weights['w4,0'] + weights['w4,1'] * inputs['Neuron 1'] + weights['w4,2'] * inputs['Neuron 2']
a4 = round(relu(z4), 2)

z5 = weights['w5,0'] + weights['w5,3'] * a3 + weights['w5,4'] * a4
a5 = round(relu(z5), 2)

z6 = weights['w6,0'] + weights['w6,3'] * a3 + weights['w6,4'] * a4
a6 = round(relu(z6), 2)
print(f'{a3}, {a4}, {a5}, {a6}')
# Print the results
print(f"Output for Neuron 5: {a5}")
print(f"Output for Neuron 6: {a6}")


#part B
# Define the desired outputs
desired_outputs = {'Neuron 5': 0.7, 'Neuron 6': 0.4}

# Calculate the squared errors
error_5 = (desired_outputs['Neuron 5'] - a5) ** 2
error_6 = (desired_outputs['Neuron 6'] - a6) ** 2

# Calculate the sum of squared errors
sse = (error_5 + error_6)

# Print the result
print(f"Sum of Squared Errors (SSE): {round(sse, 4)}")
print(f"Mean of Sum of Squared Errors (MSE): {round(sse/2, 4)}")


#part c
# Define the derivatives of the activation function
def relu_derivative(x):
    return 1 if x > 0 else 0

# Calculate error delta for output neuron 6
delta_6 = (desired_outputs['Neuron 6'] - a6) * relu_derivative(z6)

# Calculate error delta for output neuron 5
delta_5 = (desired_outputs['Neuron 5'] - a5) * relu_derivative(z5)

# Calculate error delta for hidden neuron 4
delta_4 = (weights['w6,4'] * delta_6 + weights['w5,4'] * delta_5) * relu_derivative(z4)

# Calculate error delta for hidden neuron 3
delta_3 = (weights['w6,3'] * delta_6 + weights['w5,3'] * delta_5) * relu_derivative(z3)

# Print the results
print(f"Error delta for Neuron 6: {round(delta_6, 3)}")
print(f"Error delta for Neuron 5: {round(delta_5, 2)}")
print(f"Error delta for Neuron 4: {round(delta_4, 2)}")
print(f"Error delta for Neuron 3: {-1 * round(delta_3, 2)}")



#part D
# Define the error deltas and activated outputs
delta_6 = 0.37
delta_5 = 0.538
delta_4 = -0.180
delta_3 = 0
a1 = 0.3
a2 = 0.6
a3 = 0
a4 = 0.34

# Calculate the sensitivity of the error to each weight
sensitivity_w64 = delta_6 * a4
sensitivity_w63 = delta_6 * a3
sensitivity_w60 = delta_6
sensitivity_w54 = delta_5 * a4
sensitivity_w53 = delta_5 * a3
sensitivity_w50 = delta_5
sensitivity_w42 = delta_4 * a2
sensitivity_w41 = delta_4 * a1
sensitivity_w40 = delta_4
sensitivity_w32 = delta_3 * a2
sensitivity_w31 = delta_3 * a1
sensitivity_w30 = delta_3

# Print the results
print(f"Sensitivity of Error to w6,4: {sensitivity_w64}")
print(f"Sensitivity of Error to w6,3: {sensitivity_w63}")
print(f"Sensitivity of Error to w6,0: {sensitivity_w60}")
print(f"Sensitivity of Error to w5,4: {sensitivity_w54}")
print(f"Sensitivity of Error to w5,3: {sensitivity_w53}")
print(f"Sensitivity of Error to w5,0: {sensitivity_w50}")
print(f"Sensitivity of Error to w4,2: {sensitivity_w42}")
print(f"Sensitivity of Error to w4,1: {sensitivity_w41}")
print(f"Sensitivity of Error to w4,0: {sensitivity_w40}")
print(f"Sensitivity of Error to w3,2: {sensitivity_w32}")
print(f"Sensitivity of Error to w3,1: {sensitivity_w31}")
print(f"Sensitivity of Error to w3,0: {sensitivity_w30}")


#part E
# Define the learning rate
alpha = 0.1

# Update the weights
weights['w6,4'] += alpha * delta_6 * a4
weights['w6,3'] += alpha * delta_6 * a3
weights['w6,0'] += alpha * delta_6
weights['w5,4'] += alpha * delta_5 * a4
weights['w5,3'] += alpha * delta_5 * a3
weights['w5,0'] += alpha * delta_5
weights['w4,2'] += alpha * delta_4 * a2
weights['w4,1'] += alpha * delta_4 * a1
weights['w4,0'] += alpha * delta_4
weights['w3,2'] += alpha * delta_3 * a2
weights['w3,1'] += alpha * delta_3 * a1
weights['w3,0'] += alpha * delta_3

# Print the updated weights
for key, value in weights.items():
    print(f"{key}: {value}")



#part f

# Calculate the output for each neuron
z3 = weights['w3,0'] + weights['w3,1'] * inputs['Neuron 1'] + weights['w3,2'] * inputs['Neuron 2']
a3 = round(relu(z3), 2)

z4 = weights['w4,0'] + weights['w4,1'] * inputs['Neuron 1'] + weights['w4,2'] * inputs['Neuron 2']
a4 = round(relu(z4), 2)

z5 = weights['w5,0'] + weights['w5,3'] * a3 + weights['w5,4'] * a4
a5 = round(relu(z5), 2)

z6 = weights['w6,0'] + weights['w6,3'] * a3 + weights['w6,4'] * a4
a6 = round(relu(z6), 2)
print(f'{a3}, {a4}, {a5}, {a6}')
# Print the results
print(f"Output for Neuron 5: {a5}")
print(f"Output for Neuron 6: {a6}")


#part h
# Calculate the squared errors
error_5 = (desired_outputs['Neuron 5'] - a5) ** 2
error_6 = (desired_outputs['Neuron 6'] - a6) ** 2

# Calculate the sum of squared errors
sse = (error_5 + error_6)

# Print the result
print(f"Sum of Squared Errors (SSE): {round(sse, 2)}")
print(f"Mean of Sum of Squared Errors (SSE): {round(sse/2, 2)}")

oldSSE = 0.41779
newSSE = 0.33 

print(f'Reduction in error: {oldSSE - newSSE}')



#part i, plotting the graph

# Define the SSE values at each training step
sse_values = [oldSSE, newSSE]  # Add more values if needed

# Define the training steps (you can use the x-axis for training step number)
training_steps = [0, 1]  # Add more steps if needed

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(training_steps, sse_values, marker='o', linestyle='-')
plt.title("SSE Change During Training")
plt.xlabel("Training Step")
plt.ylabel("SSE")
plt.grid(True)

# Show the plot
plt.show()



#Part 3, plotting the graph for 100 epochs.
# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Function to initialize weights randomly in the specified range
def initialize_weights():
    # Initialize weights for input layer to hidden layer
    w_input_hidden = np.random.uniform(low=-0.5, high=0.5, size=(2, 2))
    
    # Initialize weights for hidden layer to output layer
    w_hidden_output = np.random.uniform(low=-0.5, high=0.5, size=(2, 1))
    
    # Initialize biases for the hidden and output layers
    bias_hidden = np.zeros((1, 2))
    bias_output = np.zeros((1, 1))
    
    return {'w_input_hidden': w_input_hidden, 'w_hidden_output': w_hidden_output,
            'bias_hidden': bias_hidden, 'bias_output': bias_output}

# Neural network training function
def train_neural_network(inputs, desired_outputs, learning_rate, epochs):
    # Initialize weights and biases
    weights = initialize_weights()

    # Lists to store SSE values for plotting
    sse_values = []

    for epoch in range(epochs):
        # Forward pass
        hidden_inputs = np.dot(inputs, weights['w_input_hidden']) + weights['bias_hidden']
        hidden_outputs = sigmoid(hidden_inputs)

        final_inputs = np.dot(hidden_outputs, weights['w_hidden_output']) + weights['bias_output']
        final_outputs = sigmoid(final_inputs)

        # Calculate error
        errors = desired_outputs - final_outputs
        sse = 0.5 * np.sum(errors**2)
        sse_values.append(sse)

        # Backpropagation
        output_delta = errors * sigmoid_derivative(final_outputs)
        hidden_errors = np.dot(output_delta, weights['w_hidden_output'].T)
        hidden_delta = hidden_errors * sigmoid_derivative(hidden_outputs)

        # Update weights and biases
        weights['w_hidden_output'] += learning_rate * np.dot(hidden_outputs.T, output_delta)
        weights['bias_output'] += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        weights['w_input_hidden'] += learning_rate * np.dot(inputs.T, hidden_delta)
        weights['bias_hidden'] += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

    return weights, sse_values

# Define input and desired output
inputs = np.array([[0.3, 0.6]])
desired_outputs = np.array([[0.7]])

# Train the neural network
learning_rate = 0.1
epochs = 100
trained_weights, sse_values = train_neural_network(inputs, desired_outputs, learning_rate, epochs)

# Plot the sum of squared errors during training
plt.plot(range(epochs), sse_values, marker='o', linestyle='-')
plt.title("Sum of Squared Errors During Training")
plt.xlabel("Epoch")
plt.ylabel("SSE")
plt.grid(True)
plt.show()