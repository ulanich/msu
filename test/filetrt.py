import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

wave = []
intance = []
freq = []

const = {'plank': 6.63*10**(-34), 'light': 3*10**8, 'boltzmann': 1.38*10**(-23) }

def take_data(types, filename, axestype = 0, el_temp = 0, wavelenght = 0, temp = 0):
    i = 0
    line = 0
    with open(filename,'r') as f:
        for i in range (0,7):
            f.readline()
        
        for line in f:
            x = line[:-1]
            x,y = x.replace(',','.').split(';')
            wave.append(float(x))
            intance.append(float(y))

    for i in range (0,len(wave)):
        freq.append(1/wave[i])
    fig = plt.figure()
    ax = plt.subplot()
    
    if types == 0:
        ax.plot(wave, intance, color = 'r')
        ax.grid()

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Длина волны')
        ax.set_facecolor('#f4f0fc')
                
    if types == 1:
        ax.plot(freq, intance, color = 'r')
        ax.grid()

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Частота')
        ax.set_facecolor('#f4f0fc')

    if el_temp == 1:
        teoretical_spectr = []
        
        for i in range(0, len(wave)):
            teoretical_spectr.append(wavelenght**2/(wave[i]**2)*math.exp(-(const['plank']*const['light'])/(const['boltzmann']*temp)*(1/(wave[i]*10**(-9))-1/(wavelenght*10**(-9)))))
        
        for j in range (0, len(intance)):
            intance[j] = intance[j]/intance[10] #какая то залупа
        
        ax1 = plt.subplot()
        ax1.plot(wave, teoretical_spectr, color = 'b')
        
        ax.plot(wave, intance, color = 'r')
        ax.grid()

        plt.title('ОТНЕСЕННЫЙ СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('I / I(600нм)')
        plt.xlabel('Длина волны')
        ax.set_facecolor('#f4f0fc')

    if axestype == 1:
        ax.set_yscale ('log')



    wave.clear()
    intance.clear()
    freq.clear()
    plt.show()
