from numpy import array
import numpy as np

A = array([[2.12, -2.12, 51.3, 100, np.pi],
           [0.333, -0.333, -12.2, 19.7, np.sqrt(2)],
           [6.19, 8.20, -1.00, -2.01, 0],
           [-5.73, 6.12, 1, -1, -1]], dtype = float)
n = len(A)

NROW = []
S = []

for i in range(0, n):

    w1 = 0
    for j in range(0, n):
        if abs(A[i][j]) > w1:
            w1 = abs(A[i][j])
    S.append(w1)
    if S[i] == 0:
        print('no unique solution exists')
        FLAG = 0
    else:
        NROW.append(i)
        FLAG = 1

for i in range(0, n-1):

    w = 0
    for j in range(i, n):
        if abs(A[NROW[j]][i])/S[NROW[j]] > w:
            w = abs(A[NROW[j]][i])/S[NROW[j]]
            p = j
            
    if A[NROW[p]][i] == 0:
        print('no unique solution exists')
        FLAG = 0
        
    else:
        if NROW[i] != NROW[p]:
              NCOPY = NROW[i]
              NROW[i] = NROW[p]
              NROW[p] = NCOPY
              print('row', i + 1, '<-> row', p + 1, '\n')
            
        for j in range(i+1, n):
            m = (A[NROW[j]][i])/(A[NROW[i]][i])
            A[NROW[j]] = A[NROW[j]] - m*A[NROW[i]]
            FLAG = 1


if FLAG == 1:
    if A[NROW[n-1]][n-1] == 0:
        print('no unique solution exists')

    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        Xn = (A[NROW[n-1]][n] / A[NROW[n-1]][n-1])
        X = [Xn]

        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1,n):
                s = s + A[NROW[i]][j] * X[n-j-1]
            Xi = float((A[NROW[i]][n] - s)/A[NROW[i]][i])
            X.append(Xi)

        for d in range(len(X), 0, -1):
            e = n - d + 1
            f = d - 1
            print('X%d = %0.5f' %(e,X[f]), end = '\t')
