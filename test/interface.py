from tkinter import *  
from tkinter.ttk import Radiobutton 
from tkinter.filedialog import askopenfilename 
from filetrt import *
import sys

def choose_file():
    Tk().withdraw() 
    global filename
    filename = askopenfilename()
    f = filename.split("/")
    graph_b.config(state=NORMAL, bg="#a1e5a3")
    graph_temp_b.config(state=NORMAL, bg="#a1e5a3")

    zad4.config(text=f[-1:])  

def clicked(): 
    types = arg.get()
    axestype = selected.get()
    take_data(types, filename, axestype)
    
def clicked_temp():
    take_data(3, filename, 1, 1, 600, 30000)

def on_close():
    window.destroy()
    sys.exit()

window = Tk()  
window.title("Спектр")  
window.geometry('300x400') 

f_file = LabelFrame(text='Выбор файла',width=204, height=50) 
f_parameters1 = LabelFrame(text='Параметры построения спектра')
f_parameters = Frame(f_parameters1)
f_go = Frame()
f_temperature = LabelFrame(text='Температура электронов',width=204, height=50)
f_file.pack()
f_file.pack_propagate(False)
f_parameters1.pack()
f_parameters.pack()
f_go.pack()
f_temperature.pack()

open_b = Button(f_file, width=7, height=1, text="Открыть", command=choose_file)  
open_b.pack(side=LEFT)
zad4 = Label(f_file)  
zad4.pack(side=RIGHT)

zad = Label(f_parameters, text="Зависимость от:", font=("Arial Bold", 10))  
zad.pack(side=TOP)
arg = IntVar()
rad1 = Radiobutton(f_parameters, text='длины волны', value=0, variable=arg)  
rad2 = Radiobutton(f_parameters, text='частоты', value=1, variable=arg) 
rad1.pack(side=LEFT) 
rad2.pack(side=RIGHT)

zad2 = Label(f_parameters1, text="Ось Y:", font=("Arial Bold", 10))  
zad2.pack(side=TOP)
selected = IntVar()
rad3 = Radiobutton(f_parameters1, text='линейная', value=0, variable=selected)  
rad4 = Radiobutton(f_parameters1, text='логарифмическая', value=1, variable=selected) 
rad3.pack(side=LEFT)
rad4.pack(side=RIGHT)

graph_b = Button(f_go, text="Построить график", bg="#fc5d5d", width=27, height=1, command=clicked, state=DISABLED)  
graph_b.pack(side=LEFT)

graph_temp_b = Button(f_temperature, text="Построить график", bg="#fc5d5d", width=27, height=1, command=clicked_temp, state=DISABLED)  
graph_temp_b.pack()

window.protocol('WM_DELETE_WINDOW', on_close)
window.mainloop()


