from tkinter import *  
from tkinter.ttk import Radiobutton 
from tkinter.filedialog import askopenfilename 
from filetrt import *

def choose_file():
    Tk().withdraw() 
    global filename
    filename = askopenfilename()
    f = filename.split("/")
    btn2.config(state=NORMAL, bg="#a1e5a3")
    zad4.config(text=f[-1:])  

def clicked(): 
    types = arg.get()
    axestype = selected.get()
    take_data(types, filename, axestype)

window = Tk()  
window.title("Спектр")  
window.geometry('300x200') 

f_file = LabelFrame(text='Выбор файла',width=204, height=50) # root можно не указывать
f_parameters1 = LabelFrame(text='Параметры построения спектра')
f_parameters = Frame(f_parameters1)
f_go = Frame()
f_file.pack()
f_file.pack_propagate(False)
f_parameters1.pack()
f_parameters.pack()
f_go.pack()

btn1 = Button(f_file, width=7, height=1, text="Открыть", command=choose_file)  
btn1.pack(side=LEFT)
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

btn2 = Button(f_go, text="Построить график", bg="#fc5d5d", width=27, height=1, command=clicked, state=DISABLED)  
btn2.pack(side=LEFT)
window.mainloop()