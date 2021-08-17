import numpy as np
import matplotlib.pyplot as plt

# our functions f_i in the ODE y' = F(t,y)
def f1(t,x,y,z):
    return y

def f2(t,x,y,z):
    return z

def f3(t,x,y,z):
    return 4*x + 4*y - z

# exact solutions
def g1(t):
    return np.exp(-t) + np.exp(2*t) + np.exp(-2*t)

def g2(t):
    return -np.exp(-t) + 2*np.exp(2*t) - 2*np.exp(-2*t)

def g3(t):
    return np.exp(-t) + 4*np.exp(2*t) + 4*np.exp(-2*t)

# the interval of approximation
a = 0
b = 2

# initial data
x = 3
y = -1
z = 9
t = a

# steps and step size
h = 0.2
n = int((b-a)/h)

# Runge-Kutta 4th-order
WX = [x]
WY = [y]
WZ = [z]
k = 0
K = [k]
X = [x]
Y = [y]
Z = [z]
EX = [0]
EY = [0]
EZ = [0]
M = [0]
T = [t]

for i in range(n):
    K11 = h*f1(t,x,y,z)
    K12 = h*f2(t,x,y,z)
    K13 = h*f3(t,x,y,z)

    K21 = h*f1(t+h/2, x+K11/2, y+K12/2, z+K13/2)
    K22 = h*f2(t+h/2, x+K11/2, y+K12/2, z+K13/2)
    K23 = h*f3(t+h/2, x+K11/2, y+K12/2, z+K13/2)

    K31 = h*f1(t+h/2, x+K21/2, y+K22/2, z+K23/2)
    K32 = h*f2(t+h/2, x+K21/2, y+K22/2, z+K23/2)
    K33 = h*f3(t+h/2, x+K21/2, y+K22/2, z+K23/2)
    
    K41 = h*f1(t+h, x+K31, y+K32, z+K33)
    K42 = h*f2(t+h, x+K31, y+K32, z+K33)
    K43 = h*f3(t+h, x+K31, y+K32, z+K33)

    m1 = K11+2*K21+2*K31+K41
    m2 = K12+2*K22+2*K32+K42
    m3 = K13+2*K23+2*K33+K43

    x = x + m1/6
    y = y + m2/6
    z = z + m3/6

    WX.append(x)
    WY.append(y)
    WZ.append(z)

    t = t + h
    T.append(t)

    X.append(g1(t))
    Y.append(g2(t))
    Z.append(g3(t))

    EX.append(abs(x-g1(t)))
    EY.append(abs(y-g2(t)))
    EZ.append(abs(z-g3(t)))

    k = k + 1
    K.append(k)

print("\n\t n\tw1_n \t\tx(t_n)\t\tE(t_n)")
print("\t---------------------------------------------------\n")
for i in range(len(WX)):
    print("\t %d"%K[i],"\t%0.7f"%WX[i],"\t%0.7f"%X[i],"\t%0.7f"%EX[i])

print("\n\t n\tw2_n \t\ty(t_n)\t\tE(t_n)")
print("\t---------------------------------------------------\n")
for i in range(len(WY)):
    print("\t %d"%K[i],"\t%0.7f"%WY[i],"\t%0.7f"%Y[i],"\t%0.7f"%EY[i])

print("\n\t n\tw3_n \t\tz(t_n)\t\tE(t_n)")
print("\t---------------------------------------------------\n")
for i in range(len(WZ)):
    print("\t %d"%K[i],"\t%0.7f"%WZ[i],"\t%0.7f"%Z[i],"\t%0.7f"%EZ[i])
