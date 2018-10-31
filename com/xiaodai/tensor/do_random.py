# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/18 上午10:57
# @Software: PyCharm
import tensorflow as tf
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))
s=tf.assign(w1,w2,validate_shape=False)
print(s)
print(w1.assign(w2))