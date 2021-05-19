import matplotlib.pyplot as plt
from tkinter import *  
from tkinter.ttk import Radiobutton 
from tkinter.filedialog import askopenfilename 
from tkinter import scrolledtext 
import sys
import math
import numpy as np

ne = []
pressure_del = []
mach = []
ne1 = []
pressure_del1 = []
y_err = []
y_err1 = []
E_n = []
E_N = lambda p: 8.33*760*1.38*300*10**-23*10**21/p/760*300
a = 8.317016079
b = 0.000449982
a1 = 8.954043396
b1 = 0.002282174
expon = lambda x: math.exp(a1-b1*x)
def _file_still(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y,z = x.replace(',','.').split('\t')
            ne.append(float(x))
            pressure_del.append(float(y)/300*0.02898/8.31/294*10**5)
            y_err.append(float(z))
    plt.errorbar(pressure_del,ne, yerr = y_err, fmt='o', color = 'r')#, uplims= TRUE, lolims=TRUE)
    #plt.scatter(pressure_del, ne, color = "r")
    plt.title("Концентрация электронов")
    #plt.xlabel("Давление [Торр]")
    #plt.ylabel("ne - концентрация электронов [х 10^15 cm^-3]")

def _file_still_en(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y,z = x.replace(',','.').split('\t')
            ne.append(float(x))
            pressure_del.append(float(y)/300*0.02898/8.31/294*10**5)
            y_err.append(float(z))
        ro = np.linspace(10,30,100)
        for i in range(len(ro)):
            E_n.append(E_N(ro[i]))
            ro[i]*=(1/300*0.02898/8.31/294*10**5)
    plt.errorbar(pressure_del,ne, yerr = y_err, fmt='o', color = 'm', label = "Эксперимент")#, uplims= TRUE, lolims=TRUE)
    #plt.plot(ro, E_n, color = "b", label = "Рассчитанные средние значения")
    #plt.legend()
    #plt.title("Приведенное электрическое поле")

def _file_osc(filename):
    line = 0
    with open(filename,'r') as f:
        for i in range (0,20):
            f.readline()
        for line in f:
            x = line[3:-2]
            x,y = x.replace(',','.').split('\t')
            ne.append(float(x)*10**9+110)
            pressure_del.append(float(y)*50)
    plt.plot(ne, pressure_del, color = "b")
    plt.title("Осциллограмма тока")
    plt.xlabel("t, ns")
    plt.ylabel("I, A")

def _file_flow(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y,z = x.replace(',','.').split('\t')
            ne.append(float(x))
            mach.append(float(y)/300*0.02898/8.31/294*10**5) 
            y_err.append(float(z))               
    #plt.scatter(mach, ne, color = "r")
    plt.errorbar(mach,ne, yerr = y_err, fmt='o', color = 'r')#, uplims= TRUE, lolims=TRUE)
    plt.title("Концентрация электронов")
    #plt.xlabel("число Маха")
    #plt.ylabel("ne - концентрация электронов [х 10^15 cm^-3]")

def _file_energy_flow(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y = x.replace(',','.').split('\t')
            ne.append(float(x))
            mach.append(float(y)/300*0.02898/8.31/294*10**5)    
            #y_err.append(float(z))               
    #plt.errorbar(mach,ne, yerr = y_err, fmt='o', color = 'r')
    plt.scatter(mach, ne, color = "g")
    #plt.title("Энергия электронов")
    #plt.xlabel("число Маха")
    #plt.ylabel("E - энергия электронов [еВ]")

def _file_energy_still(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y,z = x.replace(',','.').split('\t')
            ne.append(float(x))
            pressure_del.append(float(y)/300*0.02898/8.31/294*10**5)
            y_err.append(float(z))               
    plt.errorbar(pressure_del,ne, yerr = y_err, fmt='o', color = 'g')
    #plt.scatter(pressure_del, ne, color = "r", marker="s")
    #plt.title("Энергия электронов")
    #plt.xlabel("Давление [Торр]")
    #plt.ylabel("E - энергия электронов [еВ]")

def _file_light(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y = x.replace(',','.').split('\t')
            ne.append(float(x))
            mach.append(float(y))
        y1 = np.linspace(610,1300,100) 
        for i in range(len(y1)):
             E_n.append(expon(y1[i]))
    plt.scatter(mach, ne, color = "r", label = 'Эксперимент')
    plt.plot(y1, E_n, color = "b", label = 'Аппроксимация')

    #plt.title("Затхуние свечения")
    plt.legend()
    #plt.xlabel("число Маха")
    #plt.ylabel("E - энергия электронов [еВ]")

def two_graphs(filename):
    line = 0
    with open(filename,'r') as f:
        for line in f:
            x = line[:-1]
            x,y,z,x1,y1,z1 = x.replace(',','.').split('\t')
            ne.append(float(x))
            pressure_del.append(float(y)/300*0.02898/8.31/294*10**5)
            y_err.append(float(z))
            ne1.append(float(x1))
            pressure_del1.append(float(y1)/300*0.02898/8.31/294*10**5)
            y_err1.append(float(z1))
    plt.errorbar(pressure_del1,ne1, yerr = y_err1, fmt='o', color = 'b')#, uplims= TRUE, lolims=TRUE)
    plt.errorbar(pressure_del,ne, yerr = y_err, fmt='o', color = 'r')#, uplims= TRUE, lolims=TRUE)
    

    #plt.scatter(pressure_del, ne, color = "r")
    plt.title("Концентрация электронов")

def choose_file():
    Tk().withdraw()
    global filename
    filename = askopenfilename()
    f = filename.split("/")
    text = ''
    text += f[-1:][0]+'\n'
    txt.insert(INSERT, text)  


def _graph(filename, _type = 0):
    if _type == 4: 
        _file_still(filename)
    elif _type == 1:
        _file_flow(filename)
    elif _type == 2:
        _file_energy_flow(filename)
    elif _type == 3:
        _file_energy_still(filename)
    elif _type == 0:
        _file_osc(filename)
    elif _type == 5:
        _file_still_en(filename)
    elif _type == 6:
        _file_light(filename)
    elif _type == 7:
        two_graphs(filename)
        
    plt.grid()
    plt.show() 

def click():
    ne.clear()
    pressure_del.clear()
    mach.clear()
    y_err.clear()
    ne1.clear()
    pressure_del1.clear()
    y_err1.clear()

    _graph(filename, arg.get())

def on_close():
    window.destroy()
    sys.exit()
window = Tk()  
window.title("Графики")  
window.geometry('300x300') 

f_file = LabelFrame(text='Выбор файла', width=204, height=55) 
f_file.pack()
f_file.pack_propagate(False)
f_parameters1 = LabelFrame(text='Параметры построения графика')
f_parameters = Frame(f_parameters1)
f_parameters1.pack()
f_parameters.pack()
f_go = Frame()
f_go.pack()

zad = Label(f_parameters, text="Тип графика:", font=("Arial Bold", 10))  
zad.pack(side=TOP)
arg = IntVar()
rad1 = Radiobutton(f_parameters, text='Концентрация электронов от плотности', value=4, variable=arg)  
rad2 = Radiobutton(f_parameters, text='Концентрация электронов от Маха', value=1, variable=arg) 
rad3 = Radiobutton(f_parameters, text='Энергия электронов от плотности', value=3, variable=arg) 
rad4 = Radiobutton(f_parameters, text='Энергия электронов от Маха', value=2, variable=arg) 
rad5 = Radiobutton(f_parameters, text='Осциллограмма тока', value=0, variable=arg) 
rad6 = Radiobutton(f_parameters, text='E/N неподвижный воздух', value=5, variable=arg) 
rad7 = Radiobutton(f_parameters, text='Затухание', value=6, variable=arg) 
rad8 = Radiobutton(f_parameters, text='2 графика', value=7, variable=arg) 

rad1.pack() 
rad2.pack()
rad3.pack() 
rad4.pack()
rad5.pack()
rad6.pack()
rad7.pack()
rad8.pack()

open_b = Button(f_file, width=7, height=1, text="Открыть", command=choose_file)  
open_b.pack(side=LEFT)
txt = scrolledtext.ScrolledText(f_file, width=12)
txt.pack(side= RIGHT)

graph_b = Button(f_go, text="Построить график", bg="#fc5d5d", width=27, height=1, command=click)  
graph_b.pack(side=LEFT)

window.protocol('WM_DELETE_WINDOW', on_close)
window.mainloop()
