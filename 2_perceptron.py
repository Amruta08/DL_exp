import numpy as np

inp = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
bias = -0.5  
wt = np.array([1, 1])

def ORs(x, wt, bias):
    fx = np.dot(wt, x) + bias
    if fx >= 0:
        return 1
    else:
        return 0

for i in inp:
    print("OR(", i, ")=", ORs(i, wt, bias))


"""
Output :-
OR( [0 0] )= 0
OR( [0 1] )= 1
OR( [1 0] )= 1
OR( [1 1] )= 1
"""