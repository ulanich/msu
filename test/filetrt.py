import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
wave = []
intance = []
freq = []
def take_data(types, filename, axestype = 0):
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

    fig, ax = plt.subplots()
    if types == 0:
        ax.plot(wave, intance,color = 'r')
        ax.grid()

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Длина волны')
        fig.set_facecolor('mintcream')
        ax.set_facecolor('whitesmoke')
                
    if types == 1:
        ax.plot(freq, intance, color = 'r')
        ax.grid()

        plt.title('СПЕКТР ИЗЛУЧЕНИЯ')
        plt.ylabel('Интенсивность')
        plt.xlabel('Частота')
        fig.set_facecolor('mintcream')
        ax.set_facecolor('whitesmoke')
    if axestype == 1:
        ax.set_yscale ('log')
    wave.clear()
    intance.clear()
    freq.clear()
    plt.show()
