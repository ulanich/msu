import numpy as np
import matplotlib.pyplot as plt


dh = 2309*10**3
cpliq = 4187
cpvap = 1874
lamliq = 0.67
nuliq = 0.335 * 10**(-3)
roliq = 971.8
d = 0.2
L = 2
mvliq = 1.3

dH = lambda x: dh+0.68*cpliq*x+cpvap*x
Re = lambda x: (3.7*lamliq*L*x/(nuliq*dH(x)*(nuliq**2/(10*roliq**2))**(1/3))+4.8)**(0.82)
hwavy = lambda x: Re(x)*lamliq/(1.08*Re(x)**(1.22)-5.2)*(10*roliq**2/nuliq**2)**(1/3)

dt = np.linspace(0,100, 1000)
f = []
for i in range (0,len(dt)):
    f.append(abs(hwavy(dt[i])*d*L*dt[i] - cpliq*10*mvliq))

print(dt[f.index(min(f))])
dT = dt[f.index(min(f))]
print(Re(24))
mvvap = hwavy(dT)*d*L*dT/dH(dT)

print(mvvap)

plt.plot(dt, f)
plt.show()