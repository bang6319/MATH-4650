import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return 1/t**2-y/t-y**2

def df(t,y):
    return 2*(y**3)+2*(y**2)/t-3/(t**3)

#def ddf(t,y):
    #return (2*(y**2)*(3*y**2-3*y+1))/((1+t)**3)

#def dddf(t,y):
    #return (2*(y**2)*(12*y**3-18*y**2+11*y-3))/((1+t)**4)

def g(t):
    return -1/t

#def ME(t):
    #return

a = 1
b = 2

h = 0.05
t = a

w2 = -1
#w4 = -(np.log(2))**(-1)
i = 0

W2 = [w2]
#W4 = [w2]
k = 0
K = [k]
X = [w2]
E = [0]
#M = [0]
T = [0]

for i in range(int((b-a)/h)):

    def T2(t,y):
        return f(t,y) + (h/2)*df(t,y)
    #def T4(t,y):
        #return f(t,y) + (h/2)*df(t,y) + ((h**2)/6)*ddf(t,y) + ((h**3)/24)*dddf(t,y)
        
    m2 = T2(t,w2)
    #m4 = T4(t,w4)
    t = t + h
    w2 = w2 + m2*h
    #w4 = w4 + m4*h
    k = k + 1
    T.append(t)
    W2.append(w2)
    #W4.append(w4)
    K.append(k)
    X.append(g(t))
    E.append(abs(w2-g(t)))
    #M.append(ME(t))

print("\n\t n\tw_n \t\tx(t_n)\t\terror")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W2)):
    print("\t %d"%K[i],"\t%0.6f"%W2[i],"\t%0.6f"%X[i],"\t%0.6f"%E[i])

# create the PL interpolation function
def PL(s):
    for i in range(int((b-a)/h)):
        aa = T[i]
        bb = T[i+1]
        if (aa <= s) and (s < bb):
            return (-1/h)*W2[i]*(s-bb)+W2[i+1]*(s-aa)/h
        elif s==T[int((b-a)/h)]:
            return W2[int((b-a)/h)]

# Use PL(t) to approximate y(t) at t1 = 0.25 and t2 = 0.93
t1 = 1.555
t2 = 1.978
TT = [t1,t2]

w1 = PL(t1)
w2 = PL(t2)
WW = [w1,w2]

y1 = g(t1)
y2 = g(t2)
YY = [y1,y2]

E1 = abs(w1-y1)
E2 = abs(w2-y2)
EE = [E1,E2]




print("\n\t 5.2.14")
print("\n\t t\tw(t) \t\ty(t)\t\terror")
print("\t--------------------------------------------------\n")
for i in range(len(EE)):
    print("\t %0.2f"%TT[i],"\t%0.6f"%WW[i],"\t%0.6f"%YY[i],"\t%0.6f"%EE[i])
