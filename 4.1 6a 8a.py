import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(2*x) - np.cos(2*x)

# Its derivatives
def fp(x):
    return 2*np.sin(2*x) + 2*(np.exp(2*x))

def fpp(x):
    return 4*(np.exp(2*x)) + 4*np.cos(2*x)

def fppp(x):
    return -8*np.sin(2*x) + 8*(np.exp(2*x))

# The sample points to be input
h = 0.1
x0 = -0.3
x1 = -0.2
x2 = -0.1
x3 = -0

# 3-point formulas
def df_mid_3(x):
    return (f(x+h)-f(x-h))/(2*h)
def df_end_3(x):
    return (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)

print("\n\t x = -0.3 \t x = -0.2 \t x = -0.1 \t x = 0")
print("\t-------------------------------------------------------------------")
print("\n\t 3-point end \t 3-point mid \t 3-point mid \t 3-point end")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%df_end_3(x0), "\t %0.6f"%df_mid_3(x1), "\t %0.6f"%df_mid_3(x2),"\t %0.6f"%df_end_3(x3))

y = [abs(df_end_3(x0)-fp(-0.3)),abs(df_mid_3(x1)-fp(-0.2)),abs(df_mid_3(x2)-fp(-0.1)),abs(df_end_3(x3)-fp(0))]
z = [abs(fppp(-0.3)*h**2/3), abs(fppp(-0.2)*h**2/6), abs(fppp(-0.1)*h**2/6), abs(fppp(0)*h**2/3)]

print("\n\n\t Actual Errors")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%y[0],"\t %0.6f"%y[1],"\t %0.6f"%y[2],"\t %0.6f"%y[3])

print("\n\n\t Theoretical Error Bounds")
print("\t-------------------------------------------------------------------")
print("\t %0.6f"%z[0],"\t %0.6f"%z[1],"\t %0.6f"%z[2],"\t %0.6f"%z[3])    


