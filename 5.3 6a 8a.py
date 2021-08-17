import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return (2 - 2*t*y)/(t**2+1)

def df(t,y):
    return 2*(3*(t**2)*y-4*t-y)/((t**2+1)**2)

def ddf(t,y):
    return 12*(-2*(t**3)*y+3*(t**2)+2*t*y-1)/((t**2+1)**3)

def dddf(t,y):
    return 24*(5*(t**4)*y-8*(t**3)-10*(t**2)*y+8*t+y)/((t**2+1)**4)

#def ME(t):
    #return

a = 0
b = 1

h = 0.1
t = a

w2 = 1
w4 = 1
i = 0

W2 = [w2]
W4 = [w2]
k = 0
K = [k]
#X = [w]
#E = [0]
#M = [0]
T = [0]

for i in range(int((b-a)/h)):

    def T2(t,y):
        return f(t,y) + (h/2)*df(t,y)
    def T4(t,y):
        return f(t,y) + (h/2)*df(t,y) + ((h**2)/6)*ddf(t,y) + ((h**3)/24)*dddf(t,y)
        
    m2 = T2(t,w2)
    m4 = T4(t,w4)
    t = t + h
    w2 = w2 + m2*h
    w4 = w4 + m4*h
    k = k + 1
    T.append(t)
    W2.append(w2)
    W4.append(w4)
    K.append(k)
    #X.append(f(t,w))
    #E.append(abs(w-g(t)))
    #M.append(ME(t))

print("\n\t n\tOrder 2 w_n \t\tOrder 4 w_n")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W4)):
    print("\t %d"%K[i],"\t%0.6f"%W2[i],"\t\t%0.6f"%W4[i])

