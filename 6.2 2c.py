from numpy import array
import numpy as np

A = array([[5, 1, -6, 7],
           [2, 1, -1, 8],
           [6, 12, 1, 9]], dtype = float)
n = len(A)

for i in range(0, n-1):

    p = None
    for b in range(i, n):
        if A[b][i] != 0:
            p = b
            break
    if p == None:
        print('no unique solution exists')
        FLAG = 0
        
    else:
        if p != i:
            A[[i, p],:] = A[[p, i],:]
            print('row', i + 1, '<-> row', p + 1, '\n')
            
        for j in range(i+1, n):
            m = (A[j][i])/(A[i][i])
            A[j] = A[j] - m*A[i]
            FLAG = 1

if FLAG == 1:
    if A[n-1][n-1] == 0:
        print('no unique solution exists')

    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        Xn = (A[n-1][n] / A[n-1][n-1])
        X = [Xn]

        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1,n):
                s = s + A[i][j] * X[n-j-1]
            Xi = float((A[i][n] - s)/A[i][i])
            X.append(Xi)

        for d in range(len(X), 0, -1):
            e = n - d + 1
            f = d - 1
            print('X%d = %0.5f' %(e,X[f]), end = '\t')