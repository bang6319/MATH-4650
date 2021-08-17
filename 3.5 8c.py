x = [0.1, 0.2, 0.3]
a = [-0.29004996, -0.56079734, -0.81401972]
n = 2
FPO = -2.8004996
FPN = -2.9734038
c = []
b = []
d = []

h = [x[i+1] - x[i] for i in range(0,n)]

al = [3*(a[1] - a[0])/h[0] - 3*FPO]
for i in range(1, n):
    al.append((3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1]))
al.append(3*FPN - 3*(a[n]-a[n-1])/h[n-1])

l = [2*(h[0])]
u = [0.5]
z = [al[0]/l[0]]

for i in range(1, n):
    l.append(2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1])
    u.append(h[i]/l[i])
    z.append((al[i] - h[i-1]*z[i-1])/l[i])

l.append(h[n-1]*(2-u[n-1]))
z.append((al[n]-h[n-1]*z[n-1])/l[n])
c = [z[n]]
C = []
B = []
D = []

for j in range(0,n):
    c.append(z[n-1-j] - u[n-1-j]*c[j])
    b.append((a[n-j] - a[n-1-j])/h[n-1-j] - h[n-1-j]*(c[j] + 2*c[j+1])/3)
    d.append((c[j] - c[j+1])/(3*h[n-1-j]))

for j in range(0,n):
    C.append(c[n-j])
    B.append(b[n-1-j])
    D.append(d[n-1-j])

for j in range(0,n):
    print("a[",j,"] = ",a[j],\
          "b[",j,"] = ",B[j],\
          "c[",j,"] = ",C[j],\
          "d[",j,"] = ",D[j])
