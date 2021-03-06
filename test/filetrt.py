import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

wave = []
intance = []
freq = []

const = {'plank': 6.63*10**(-34), 'light': 3*10**8, 'boltzmann': 1.38*10**(-23) }

def take_data(types, filename, axestype = 0, el_temp = 0, wavelenght = 0, temp = 0):
    
    for k in range(0,len(filename)):
        i = 0
        line = 0
        with open(filename[k],'r') as f:
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
            ax = plt.subplot()
            _max = max(intance[820:829])
            max_ = []
            for i in range (len(wave)): max_.append(_max/2)
            ax.plot(wave, intance, color = 'r')
            ax.plot(wave, max_, color = 'g')
            ax.grid()

            plt.title('СПЕКТР ИЗЛУЧЕНИЯ, файл: %s' %filename[k][-11:])
            plt.ylabel('Интенсивность')
            plt.xlabel('Длина волны')
            ax.set_facecolor('#f4f0fc')
                    
        if types == 1:
            ax = plt.subplot()
            ax.plot(freq, intance, color = 'r')
            ax.grid()

            plt.title('СПЕКТР ИЗЛУЧЕНИЯ, файл: %s' %filename[k][-11:])
            plt.ylabel('Интенсивность')
            plt.xlabel('Частота')
            ax.set_facecolor('#f4f0fc')

        if el_temp == 1:
            teoretical_spectr = []
            
            for i in range(0, len(wave)):
                teoretical_spectr.append(wavelenght**2/(wave[i]**2)*math.exp(-(const['plank']*const['light'])/(const['boltzmann']*temp)*(1/(wave[i]*10**(-9))-1/(wavelenght*10**(-9)))))
            
            i = 0
            
            while abs(wave[i]-wavelenght) > 0.6:
                i+=1
            
            att_intence = intance[i]

            for j in range (0, len(intance)):
                intance[j] = intance[j]/att_intence 
            
            ax1 = plt.subplot()
            ax1.plot(wave, teoretical_spectr, color = 'b')
            
            ax.plot(wave, intance, color = 'r')
            ax.grid()

            plt.title('ОТНЕСЕННЫЙ СПЕКТР ИЗЛУЧЕНИЯ, файл: %s' %filename[k][-11:])
            plt.ylabel('I / I(%dнм)' %wavelenght)
            plt.xlabel('Длина волны')
            ax.set_facecolor('#f4f0fc')

        if axestype == 1:
            ax.set_yscale ('log')



        wave.clear()
        intance.clear()
        freq.clear()
    plt.show()
