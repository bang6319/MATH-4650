from numpy import array
import numpy as np

A = array([[2,2,4,5],
           [1,-1,1,7],
           [1,1,-1,2],
           [2,3,4,6]], dtype = float)
n = len(A)

l = [[0.0] * n for a in range(0,n)]
u = [[0.0] * n for a in range(0,n)]

for b in range (0, n):
    l[b][b] = 1.0

u[0][0] = A[0][0]/l[0][0]

if (l[0][0]*u[0][0] == 0):
    print('Fractorization imposible')
    FLAG = 0

else:
    for j in range (1, n):
        u[0][j] = A[0][j]/l[0][0]
        l[j][0] = A[j][0]/u[0][0]

    for i in range (1, n-1):
        s = 0
        for k in range(0,i):
            s = s + l[i][k]*u[k][i]

        u[i][i] = (A[i][i] - s)/l[i][i]
        
        if (l[i][i]*u[i][i] == 0):
            print('Fractorization imposible')
            FLAG = 0
            break
        else:
            for j in range (i+1, n):
                s1 = 0
                s2 = 0
                for k in range(0,i):
                    s1 = s1 + l[i][k]*u[k][j]
                    s2 = s2 + l[j][k]*u[k][i]
                u[i][j] = (1/l[i][i])*(A[i][j] - s1)
                l[j][i] = (1/u[i][i])*(A[j][i] - s2)
                FLAG = 1

if FLAG == 1:

    s3 = 0
    for k in range(0,n-1):
        s3 = s3 + l[n-1][k]*u[k][n-1]

    u[n-1][n-1] = (A[n-1][n-1] - s3)/l[n-1][n-1]
    
    print('L =', l)

    print('\t')
                
    print('U =', u)
