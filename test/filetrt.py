import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
wave = []
intance = []
freq = []
def take_data(types, filename):
    i = 0
    line = 0
    with open(filename,'r') as f:
        for i in range (0,7):
            f.readline()
        for line in f:
            x = f.readline()[:-1]
            x,y = x.replace(',','.').split(';')
            wave.append(float(x))
            intance.append(float(y))

    for i in range (0,len(wave)):
        freq.append(1/wave[i])

    if types == 1:
        fig = plt.figure()
        plt.plot(wave, intance)

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Длина волны')

        
    if types == 2:
        fig = plt.figure()
        plt.plot(freq, intance)

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Частота')
    wave.clear()
    intance.clear()
    freq.clear()
    plt.show()
