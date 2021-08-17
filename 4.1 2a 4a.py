import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*np.cos(2*x) - x

# Its derivatives
def fp(x):
    return -4*np.sin(2*x) - 1

def fpp(x):
    return -8*np.cos(2*x)

# The sample points to be input
h = 0.1
x0 = -0.3
x1 = -0.3
x2 = -0.2

# 2-point formula 
df = [(f(x0+h)-f(x0))/h, (f(x1+h)-f(x1))/h, (f(x2+h)-f(x2))/h]

print("\n\t x = -0.3 \t x = -0.2 \t x = -0.1")
print("\t-------------------------------------------------------------------")
print("\n\t 2-point")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%df[0], "\t %0.6f"%df[1], "\t %0.6f"%df[2])
    
y = [abs(df[0]-fp(-0.3)),abs(df[1]-fp(-0.2)),abs(df[2]-fp(-0.1))]
z = [abs(fpp(-0.2)*h/2), abs(fpp(-0.2)*h/2), abs(fpp(-0.1)*h/2)]

print("\n\n\t Actual Errors")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%y[0],"\t %0.6f"%y[1],"\t %0.6f"%y[2])

print("\n\n\t Theoretical Error Bounds")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%z[0],"\t %0.6f"%z[1],"\t %0.6f"%z[2])

