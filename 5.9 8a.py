import numpy as np
import matplotlib.pyplot as plt

# our functions f_i in the ODE y' = F(t,y)
def f1(t,x,y):
    return y

def f2(t,x,y):
    return -16.085*np.sin(x)

# exact solutions
#def g1(t):
 #   return (-1/2)*(np.exp(2*t)) + t**2 + 2*t - 1/2

#def g2(t):
 #   return (1/2)*(np.exp(2*t)) + t**2 - 1/2

# the interval of approximation
a = 0
b = 2

# initial data
x = np.pi/6
y = 0
t = a

# steps and step size
h = 0.1
n = int((b-a)/h)

# Runge-Kutta 4th-order
WX = [x]
WY = [y]
k = 0
K = [k]
#X = [x]
#Y = [y]
#EX = [0]
#EY = [0]
M = [0]
T = [t]

for i in range(n):
    K11 = h*f1(t,x,y)
    K12 = h*f2(t,x,y)

    K21 = h*f1(t+h/2, x+K11/2, y+K12/2)
    K22 = h*f2(t+h/2, x+K11/2, y+K12/2)

    K31 = h*f1(t+h/2, x+K21/2, y+K22/2)
    K32 = h*f2(t+h/2, x+K21/2, y+K22/2)
    
    K41 = h*f1(t+h, x+K31, y+K32)
    K42 = h*f2(t+h, x+K31, y+K32)

    m1 = K11+2*K21+2*K31+K41
    m2 = K12+2*K22+2*K32+K42

    x = x + m1/6
    y = y + m2/6

    WX.append(x)
    WY.append(y)

    t = t + h
    T.append(t)

    #X.append(g1(t))
    #Y.append(g2(t))

    #EX.append(abs(x-g1(t)))
    #EY.append(abs(y-g2(t)))

    k = k + 1
    K.append(k)

print("\n\t n\tw1_n \t\tw2_n")
print("\t---------------------------------------------------\n")
for i in range(len(WX)):
    print("\t %d"%K[i],"\t%0.7f"%WX[i],"\t%0.7f"%WY[i])
