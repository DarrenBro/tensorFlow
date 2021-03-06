import tensorflow as tf
import numpy as np
from tensorflow import keras

# Keras is an open-source neural-network library written in Python
# The Sequential model API is a way of creating deep learning models where an instance of the Sequential class is
# created and model layers are created and added to it.
# The Sequential model is a linear stack of layers.

# The simplest possible trained neural network(aka model) has 1 layer, 1 neuron(units). Input shape is 1 value.
# Shown by keras.layers.Dense
# Single value for X => input_shape=[1]
# This line defines the model itself.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# We'll have the Neural network predict what Y would be for X

# You must compile your model before training/testing. Otherwise it's a runtime error.
# loss function determines how good/bad a guess is while training
# model.compile(optimizer='sgd', loss='mean_squared_error')

# Both loss and optimizer are functions
# optimizer function generates each guess and lets us add training parameters
# and the optimiser, which sgd = Stochastic gradient descent (popular) - stuh · ka · stick
sgd = tf.optimizers.SGD(lr=0.01)
model.compile(
    # Computes the mean squared error between y_true and y_pred. e.g. loss: 2.2777e-09
    loss='mean_squared_error',
    optimizer='sgd',
)

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
# Y = 2X - 1

# Epochs is our loops of training and evaluating
# Fit the Xs to the Ys
model.fit(xs, ys, epochs=1000)

# predict y when x = 10
# What do we expect?
# Y = 2(10) - 1
# We would hope to predict 19, but value 10 for x has never bee seen before,
# even if the relationship is linear how certain can a model be?
print(model.predict([10.0]))

# Result explained
# Epoch 500/500

# 6/6 = 6 X an Y
# 143us/sample =

# loss: Closer the loss value is to 0 the better the inferring(conclusion) for relationship between the numbers:
# We use a loss function to determine how far the predicted values deviate from the actual values in the training data.
# We change the model weights to make the loss minimum, and that is what training is all about.

# 6/6 [==============================] - 0s 143us/sample - loss: 5.5802e-05
# [[18.978205]]