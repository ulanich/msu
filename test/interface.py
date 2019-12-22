from tkinter import *  
from tkinter.ttk import Radiobutton 
from tkinter.filedialog import askopenfilename 
from filetrt import *

def choose_file():
    Tk().withdraw() 
    global filename
    filename = askopenfilename()# разделить для нескольких графиков
    btn2.config(state=NORMAL)
    
def clicked(): 
    types = arg.get()
    axestype = selected.get()
    take_data(types, filename, axestype)

window = Tk()  
window.title("Спектр")  
window.geometry('350x190')  

zad1 = Label(window, text="Выберите файл",  font=("Arial Bold", 12))  
zad1.grid(column=1, row=0) 

btn1 = Button(window, text="    Файл    ", command=choose_file)  
btn1.grid(column=1, row=1)   

zad = Label(window, text="Зависимость от:", font=("Arial Bold", 12))  
zad.grid(column=1, row=2) 
arg = IntVar()
rad1 = Radiobutton(window, text='длины волны', value=0, variable=arg)  
rad2 = Radiobutton(window, text='частоты', value=1, variable=arg) 
rad1.grid(column=0, row=3)  
rad2.grid(column=2, row=3)

zad2 = Label(window, text="Ось Y:", font=("Arial Bold", 12))  
zad2.grid(column=1, row=4) 
selected = IntVar()
rad3 = Radiobutton(window, text='линейная', value=0, variable=selected)  
rad4 = Radiobutton(window, text='логарифмическая', value=1, variable=selected) 
rad3.grid(column=0, row=5)  
rad4.grid(column=2, row=5) 

btn2 = Button(window, text="Построить график", command=clicked, state=DISABLED)  
btn2.grid(column=1, row=6)  
window.mainloop()