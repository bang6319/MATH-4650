# Hermite Interpolation
# Example 3.4.2 in our book


# Given x, y and y' values
x = [0, 3, 5, 8, 13]
y = [0, 225, 383, 623, 993]
w = [75, 77, 80, 74, 72]

# Define n
n=len(x)

# List Q will be a list of empty lists which we will fill below
Q = [[] for i in range(2*n)]

# Splice x with itself to form the z's
z = []
for i in range(len(x)):
    z.append(x[i])
    z.append(x[i])

# Splice y with itself to form the corresponding y-values of f on the z's
A = []
for i in range(len(y)):
    A.append(y[i])
    A.append(y[i])

# Q[0] will be our z-list
Q[0] = z

# Q[1] will be half of our first divided differences. We will splice the other half--the derivatives w--with this half. 
B = []
for i in range(1,n):
    B.append((A[2*i]-A[2*i-1])/(z[2*i]-z[2*i-1]))

C = []
for i in range(1,n):
    C.append(w[i-1])
    C.append(B[i-1])
C.append(w[n-1])

Q[1] = C

# Interpolating point
xp = 10

# Implementing Newton's Divided Differences Method
for i in range(2,2*n):
    for j in range(i,2*n):
        zi = z[j]
        zij = z[j-i]
        Qij = Q[i]
        R = Q[i-1]
        s = (R[j-i+1]-R[j-i])/(zi-zij)
        Qij.append(s)
    Q[i]=Qij

# Displaying output
for i in range(2*n):
    T = ["" for k in range(i)]
    Q[i]=T+Q[i]

Q[0] = A
S = [[] for i in range(2*n)]

for i in range(2*n):
    for j in range(2*n):
        S[i].append(Q[j][i])

for i in range(2*n):
    print("\t",format(S[i][0], ".7f") if type(S[i][0])==float else "",\
          "\t",format(S[i][1], ".7f") if type(S[i][1])==float else "",\
          "\t",format(S[i][2], ".7f") if type(S[i][2])==float else "",\
          "\t",format(S[i][3], ".7f") if type(S[i][3])==float else "",\
          "\t",format(S[i][4], ".7f") if type(S[i][4])==float else "",\
          "\t",format(S[i][5], ".7f") if type(S[i][5])==float else "",\
          "\t",format(S[i][6], ".7f") if type(S[i][6])==float else "",\
          "\t",format(S[i][7], ".7f") if type(S[i][7])==float else "",\
          "\t",format(S[i][8], ".7f") if type(S[i][8])==float else "",\
          "\t",format(S[i][9], ".7f") if type(S[i][9])==float else "")

# Evaluating at xp
yp = S[0][0]

for i in range(1,2*n):
    p = 1
    for j in range(i):
        p = p*(xp-z[j])
    yp = yp + S[i][i]*p
    
print("\n\t p(10) = %0.7f"%yp)
