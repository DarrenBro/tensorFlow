import tensorflow as tf
import numpy as np
from tensorflow import keras

# X = -1.0, 0.0, 1.0, 2.0, 3.0, 4.0
# Y = -3.0, -1.0, 1.0, 3.0, 5.0, 7.0

# y = 2x - 1

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

sgd = tf.optimizers.SGD(lr=0.01)
model.compile(
    loss='mean_squared_error',
    optimizer='sgd'
)

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=1000)

print(model.predict([10.0]))

# predict y when x = 10
# expect 19 !
