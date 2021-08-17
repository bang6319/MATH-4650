from numpy import array
import numpy as np

A = array([[-1, 4, 1, 8],
           [5/3, 2/3, 2/3, 1],
           [2, 1, 4, 11]])
n = 3


for i, j in range(0, n):
    L[i][j] = 1
    U[i][j] = 1

if L[0][0] * U[0][0] == 0:
    print('Factorization impossiple')
    FLAG = 0

else:

    for j in range(1, n):
        U[1][j] = A[0][j]/L[0][0]
        L[j][1] = A[j][0]/U[0][0]

    for i in range(1, n-1):

        if L[i][i] * U[i][i] == 0:
            print('Factorization impossiple')
            
        else:
            for j in range(i+1, n):
                s1 = 0
                for k in range(1, i-1):
                    s1 = s1 + L[i][k] * U[k][j]
                I[i][j] = (1/L[i][i]) * (a[i][j] - s1)
                s2 = 0
                for k in range(1, i-1):
                    s2 = s2 + L[j][k] * U[k][i]
                L[i][j] = (1/U[i][i]) * (a[j][i] - s2)
                
    for i in range(0, n):
        for j in range(0, i):
            print('X%d = %0.5f' %(L[i][j]), end = '\t')
            print('X%d = %0.5f' %(U[i][j]), end = '\t')
