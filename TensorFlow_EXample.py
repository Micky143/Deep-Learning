import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)

c = a * b

sess = tf.Session()

print(sess.run(c))

###------------------------------------------------------------------------------------------------------------

import tensorflow as tf

node1 =  tf.constant(3.0, tf.float64)
node2 = tf.constant(4.0)

print(sess.run([node1,node2]))
sess.close()

with tf.Session() as sess:
     output = sess.run([node1,node2])
     print(output)

#------------------------------------------------------------------------------------------------------------

import tensorflow as tf

node1 =  tf.constant(3.0, tf.float64)
node2 = tf.constant(4.0)

print(node1,node2)

#------------------------------------------------------------------------------------------------------------

import tensorflow as tf

node1 =  tf.constant(3.0, tf.float64)
node2 = tf.constant(4.0)

sess = tf.Session()
print(sess.run([node1,node2]))
sess.close()


#------------------------------------------------------------------------------------------------------------


import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)

c = a * b

sess = tf.Session()

File_Writer = tf.summary.Filewriter('Give The Tensor flow path')
# after writen this line goto the command prompt write that line
# 

print(sess.run(c))


