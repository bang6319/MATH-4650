import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2)*(np.cos(x))-3*x

def S(x):
    return -0.29 - 2.7513*(x-0.1) + 4.3813*((x-0.1)**3)

# derivatives
def df(x):
    return -(x**2)*(np.sin(x)) + 2*x*(np.cos(x)) - 3

def dS(x):
    return -2.7513 + 13.1439*((x-0.1)**2)

e1 = abs(f(0.18)-S(0.18))
e2 = abs(df(0.18)-dS(0.18))

print("\n\t S(0.18) \t f(0.18) \t Error")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%S(0.18), "\t %0.6f"%f(0.18), "\t %0.6f"%e1)

print("\n\t S'(0.18) \t f'(0.18) \t Error")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%dS(0.18), "\t %0.6f"%df(0.18), "\t %0.6f"%e2)
