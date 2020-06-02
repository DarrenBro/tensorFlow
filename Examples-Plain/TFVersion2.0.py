import tensorflow as tf
tf.enable_eager_execution()

# Construction Phase
a = tf.contrib.eager.Variable(0.)
b = tf.contrib.eager.Variable(1.)

# Execution Phase
for iteration in range(10):
    a.assign(a + b)
    b.assign(b * 2)

# NumPy is a Python library for mathematical operations.
print(a.numpy())
