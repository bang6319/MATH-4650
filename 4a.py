from numpy import array
import numpy as np

A = array([[4,2,2],
           [2,6,2],
           [2,2,5]], dtype = float)

def ldl(A):
    n = len(A)

    L = [[0.0] * n for a in range(0,n)]
    D = [0.0 * n for a in range(0,n)]

    for b in range (0, n):
        L[b][b] = 1.0

    for i in range(0,n):
        v = [L[i][j]*D[j] for j in range(0, i)]
        D[i] = A[i][i] - sum([L[i][j]*v[j] for j in range(i)])
        for j in range(i + 1, n):
            L[j][i] = (A[j,i] - sum([L[j][k]*v[k] for k in range(i)])) / D[i]
            
    print('L =', L)

    print('\t')
                
    print('D =',D)
    

ldl(A)
