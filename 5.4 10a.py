import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return np.exp(t-y)

def g(t):
    return np.log(np.exp(t) + np.e - 1)

#def ME(t):
    #return

a = 0
b = 1

h = 0.5
t = a

w = 1
i = 0

W = [w]
k = 0
K = [k]
X = [w]
E = [0]
M = [0]
T = [0]

for i in range(int((b-a)/h)):
    m = f(t,w)
    w = w + (h/4)*(m + 3*f(t + 2*(h/3), w + 2*(h/3)*f(t + h/3, w + (h/3)*m)))
    t = t + h
    k = k + 1
    T.append(t)
    W.append(w)
    K.append(k)
    X.append(g(t))
    E.append(abs(w-g(t)))
    #M.append(ME(t))

print("\n\t n\tw_n \t\tx(t_n)\t\terror")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W)):
    print("\t %d"%K[i],"\t%0.6f"%W[i],"\t%0.6f"%X[i],"\t%0.6f"%E[i])

