# X = -1, 0, 1, 2, 3, 4
# Y = -3, -1, 1, 3, 5, 7

# y = 2x - 1

import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(loss='mean_squared_error', optimizer='sgd')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

# predict y when x = 10
# 19

print(model.predict([10.0]))

