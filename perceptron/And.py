import numpy as np

def AND(x, y):
    x = np.array([x, y])
    w = np.array([0.5, 0.5])
    b = -0.8
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1