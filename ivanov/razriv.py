import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

timeres = 1.0

pmax = 8
pmin = 2 #мм рт. ст.
Smax = 150
Smin = 50

p = lambda S: (pmax-pmin)*(S-Smin)/(Smax-Smin)
k = (pmax-pmin)/(Smax-Smin)

Time = 0
xmin = 0
xmax = 0.4
tmin = 0
Nx = 50

if timeres == 1.0: 
    Nt = 126
    tmax = 1.0
elif timeres == 2.0:
    Nt = 250
    tmax = 2.0
elif timeres == 3.0:
    Nt = 378
    tmax = 3.0

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

        if j == 4:
            print('4')
        if (S[j,i+1] <= 0) | (S[j,i] <= 0):
            print ('error zero')

        Sr = max(u[j,i+1]+(k*S[j,i+1])**(1/2), u[j,i]+(k*S[j,i])**(1/2))
        Sl = min(u[j,i+1]-(k*S[j,i+1])**(1/2), u[j,i]-(k*S[j,i])**(1/2))

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
    global Time
    for i in range(0,Nt-1):
        HLL(i)

        dt = dx/max(SR,SL)+0.1*dx/max(SR,SL)
        Time += dt
        if Time >= tmax:
            print(i)
            break
        for j in range(1,Nx+1):
            u[i+1,j] = u[i,j]-dt/dx*(uS[j]-uS[j-1])
            S[i+1,j] = S[i,j]-dt/dx*(u2p[j]-u2p[j-1])
        u[i+1,0] = 0.1
        S[i+1,0] = S[i+1,1]
        u[i+1,Nx+1] = u[i+1,Nx]
        S[i+1,Nx+1] = S[i+1,Nx]

GOD()

#u[1,16] = u[1,15]

t = np.linspace(0,tmax,Nt)
x = np.linspace(0,xmax,Nx+2)

xgrid, tgrid = np.meshgrid(x,t)
fig = plt.figure()
axes = Axes3D(fig)

axes.plot_surface(tgrid, xgrid, u)
axes.set_xlabel('time')
axes.set_ylabel('X coordinate')
axes.set_zlabel('U')

fig1 = plt.figure()
axes1 = Axes3D(fig1)

axes1.plot_surface(tgrid, xgrid, S)
axes1.set_xlabel('time')
axes1.set_ylabel('X coordinate')
axes1.set_zlabel('S')

fig2 = plt.figure()

plt.plot(x,u[25], label = '%1.2f с' %t[25])
plt.plot(x, u[Nt//2], label = '%1.2f с' %t[Nt//2])
plt.plot(x, u[Nt-1], label = '%1.2f с' %t[Nt-1])
plt.title('Зависимость U от координаты')
plt.xlabel('X coorditane')
plt.ylabel('U')
plt.legend()
plt.grid()

fig3 = plt.figure()

plt.plot(x,S[25], label = '%1.2f с' %t[25])
plt.plot(x, S[Nt//2], label = '%1.2f с' %t[Nt//2])
plt.plot(x, S[Nt-1], label = '%1.2f с' %t[Nt-1])
plt.title('Зависимость S от координаты')
plt.xlabel('X coorditane')
plt.ylabel('S')
plt.legend()
plt.grid()

plt.show()
