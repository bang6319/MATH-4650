from numpy import array
import numpy as np

A = array([[4,2,2],
           [2,6,2],
           [2,2,5]], dtype = float)


def cholesky(A):

    n = len(A)

    L = [[0.0] * n for A in range(0,n)]

    L[0][0] = np.sqrt(A[0][0])

    for j in range(1,n):
        L[j][0] = A[j][0]/L[0][0]
    
    for i in range(1,n-1):
        L[i][i] = (A[i][i] - sum([L[i][k]**2 for k in range(0,i)]))**(1/2)
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum([L[j][k]*L[i][k] for k in range(0, i)]))/L[i][i]
        L[n-1][n-1] = (A[n-1][n-1] - sum([L[n-1][k]**2 for k in range(0, n - 1)]))**(1/2)
            
    print('L =', L)
    
cholesky(A)
