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

def OR(x, y):
    x = np.array([x, y])
    w = np.array([0.5, 0.5])
    b = -0.3
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NAND(x, y):
    x = np.array([x, y])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NOR(x, y):
    x1 = NAND(x, y)
    x2 = OR(x, y)
    return AND(x1, x2)