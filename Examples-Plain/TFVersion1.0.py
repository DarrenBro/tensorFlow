import tensorflow as tf

a = tf.Variable(0.)
b = tf.Variable(1.)

op_add = a.assign(a + b)
op_mul = b.assign(b * 2)
init = tf.global_variables_initializer

with tf.Session() as sess:
    init.run()
    for iteration in range(10):
        sess.run(op_add)
        sess.run(op_mul)
    print(a.eval())
