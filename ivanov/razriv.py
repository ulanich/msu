import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

pmax = 80.0
pmin = 20.0 #мм рт. ст.
Smax = 0.015
Smin = 0.005
p = lambda S: (pmax-pmin)*(S-Smin)/(Smax-Smin)
k = (pmax-pmin)/(Smax-Smin)

tmin = 0
tmax = 1.0
xmin = 0
xmax = 0.4

Nt = 10
Nx = 100

dx = (xmax - xmin)/ Nx

S = np.array([0.0]*(Nt*(Nx+2))).reshape(Nt, Nx+2)
u = np.array([0.0]*(Nt*(Nx+2))).reshape(Nt, Nx+2)
uS = np.array([0.0]*(Nx+1))
u2p = np.array([0.0]*(Nx+1))

SR = 0
SL = 0
#краевые условия

for i in range (0,Nt):
    u[i, 0] = 0.1
    u[i, 1] = 0.1

#начальные условия
for i in range (0,Nx+2):
    if i < (Nx+2)/2:
        S[0,i] = 0.02
    else:
        S[0,i] = 0.01

    u[0,i] = 0.1

def HLL(j):
    global SR, SL
    for i in range(0,len(uS)):
        Sr = max(u[j,i+1]+(k*S[j,i+1])**(1/2), u[j,i]+(k*S[j,i])**(1/2))
        Sl = max(u[j,i+1]-(k*S[j,i+1])**(1/2), u[j,i]-(k*S[j,i])**(1/2))

        if (abs(Sr)>abs(SR)): SR = abs(Sr)
        if (abs(Sl)>abs(SL)): SL = abs(Sl)

        if Sl>=0:
            uS[i] = u[j,i]*S[j,i]
            u2p[i] = u[j,i]**2/2+p(S[j,i])
        elif Sr<=0:
            uS[i] = u[j,i+1]*S[j,i+1]
            u2p[i] = u[j,i+1]**2/2+p(S[j,i+1])
        elif (Sl<0) & (Sr>0):
            uS[i] = (Sr*u[j,i]*S[j,i] - Sl*u[j,i+1]*S[j,i+1]+Sl*Sr*(u[j,i+1]-u[j,i]))/(Sr-Sl)
            u2p[i] = (Sr*(u[j,i]**2/2+p(S[j,i]))-Sl*(u[j,i+1]**2/2+p(S[j,i+1]))+Sl*Sr*(S[j,i+1]-S[j,i]))/(Sr-Sl)

def GOD():
    
    for i in range(0,Nt-1):
        HLL(i)

        dt = dx/max(SR,SL)+0.1*dx/max(SR,SL)
        for j in range(1,Nx+1):
            u[i+1,j] = u[i,j]-dt/dx*(uS[j]-uS[j-1])
            u[i+1,0] = 0.1
            S[i+1,j] = S[i,j]-dt/dx*(u2p[j]-u2p[j-1])
            S[i+1,0] = 0.02
        u[i+1,Nx+1] = u[i+1,Nx]
        S[i+1,Nx+1] = S[i+1,Nx]
        print ('u')
        for k in range(0,Nx+2):
            print(u[i+1,k])
        print('S')
        for k in range(0,Nx+2):
            print(S[i+1,k])
        print('---')

print ('u')
for k in range(0,Nx+2):
    print(u[0,k])
print('S')
for k in range(0,Nx+2):
    print(S[0,k])
print('---')
GOD()

print(u)
print(S)
'''
t = [0,1,2,3,4,5]
x = [0,1,2,3,4,5,7,8,10]

z = np.array([0.0]*(5*(10))).reshape(10, 5)

t = np.linspace(0,1,5)
x = np.linspace(0,1, 10)

tgrid, xgrid = np.meshgrid(t,x)
print (tgrid)
print(xgrid)
print(z)

fig = plt.figure()
axes = Axes3D(fig)

axes.plot_surface(tgrid, xgrid, z)

plt.show()
'''