import tensorflow as tf
a = tf.constant(3.0)
b = tf.constant(4.0)
c = tf.add(a,b)
print(c)
sess = tf.Session()
print(sess.run(c))

writer = tf.summary.FileWriter("graph", sess.graph)
