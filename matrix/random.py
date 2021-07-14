import random
import matrix.linalg as lg
from matrix.array import Matrix

def rand(shape):
    temp = lg.zero(shape[0], shape[1])
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            temp[i, j] = random.random()
    return temp


def randn(shape):
    pass

def randint(low, high, shape):
    temp = lg.zero(shape[0], shape[1])
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            temp[i, j] = random.randint(low, high - 1)
    return temp