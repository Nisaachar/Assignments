import numpy as np
import matplotlib.pyplot as plt

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
