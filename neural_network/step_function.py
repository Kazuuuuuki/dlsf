import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_max = np.max(x)
    exp_a = np.exp(x - exp_max)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

