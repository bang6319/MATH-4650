import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(np.log(x+1))

a = -0.5
b = 0

y0 = 3/4 - (6*np.log(2)+7)/16
EL = []
ER = []
EM = []
ET = []
ES = []

ML = []
MR = []
MM = []
MT = []
MS = []

W = 10
N = [2*k for k in range(1,W+1)]

print(" n\t L_n \t\t R_n \t\t M_n \t\t T_n \t\t S_n")
print("---------------------------------------------------------------------------------")
for n in N:

    L = 0
    R = 0
    M = 0
    T = 0
    S = 0

    x = []
    m = []
    dx = (b-a)/n
    
    for i in range(n+1):
        x.append(a+i*dx)

    for j in range(n):
        m.append((x[j+1]+x[j])/2)

    for k in range(n):
        L = L + f(x[k])*dx
        R = R + f(x[k+1])*dx
        M = M + f(m[k])*dx
        T = T + (f(x[k+1])+f(x[k]))*dx/2

    nn = int(n/2)
    for l in range(1,nn+1):
        S = S+(f(x[2*l-2])+4*f(x[2*l-1])+f(x[2*l]))*dx/3

    EL.append(abs(L-y0))
    ER.append(abs(R-y0))
    EM.append(abs(M-y0))
    ET.append(abs(T-y0))
    ES.append(abs(S-y0))
    
    print(" %d"%n,"\t %0.5f"%L,"\t %0.5f"%R,"\t %0.5f"%M,"\t %0.5f"%T,"\t %0.5f"%S)

print("\n\nn\t EL_n \t\t ER_n \t\t EM_n \t\t ET_n \t\t ES_n")
print("---------------------------------------------------------------------------------")    
for i in range(W):
    print("%d"%N[i],"\t %0.5f"%EL[i],"\t %0.5f"%ER[i],"\t %0.5f"%EM[i],"\t %0.5f"%ET[i],"\t %0.5f"%ES[i])

