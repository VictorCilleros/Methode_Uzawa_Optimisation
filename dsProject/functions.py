
import numpy as np

def calcul_f(x1,x2):
    f1 = lambda x, y: x**2+y**2-1
    f2 = lambda x, y: 2*x-1
    f=lambda x1,x2 : np.array([f1(x1,x2),f2(x1,x2)])
    return f(x1,x2)

