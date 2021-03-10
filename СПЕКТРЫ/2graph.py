import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

wave = []
intance1 = []
teoretical = []
const = {'plank': 6.63*10**(-34), 'light': 3*10**8, 'boltzmann': 1.38*10**(-23) }


filename = ['NEW0003.txt', 'NEW0005.txt']

Temp = 14000
C = 1000000000000*0.4
with open(filename[0],'r') as f:
    for i in range (0,7):
        f.readline()
    
    for line in f:
        x = line[:-1]
        x,y = x.replace(',','.').split(';')
        wave.append(float(x))
        intance1.append(float(y))
for i in range(0, len(intance1)):
    intance1[i] -= 800.0

for i in range(0, len(wave)):
    teoretical.append(C/(wave[i]**2*Temp**(1/2))*math.exp(-(const['plank']*const['light'])/(const['boltzmann']*Temp)*(1/(wave[i]*10**(-9)))))



fig = plt.figure()
ax = plt.subplot()
ax1 = plt.subplot()
ax.plot(wave, intance1, color = 'r', label='1')
ax1.plot(wave, teoretical, color = 'b', label ='2')
ax.grid()
'''
plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
plt.ylabel('ИНТЕНСИВНОСТЬ, отн. ед.')
plt.xlabel('ДЛИНА ВОЛНЫ, нм')
'''
ax.set_facecolor('#f4f0fc')
plt.legend(('1','2'), loc = (0.8, 0.8))
plt.show()
