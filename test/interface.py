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
    types = selected.get()
    take_data(types, filename)
  
  
window = Tk()  
window.title("Спектр")  
window.geometry('290x150')  

zad1 = Label(window, text="Выберите файл")  
zad1.grid(column=1, row=0) 

btn1 = Button(window, text="    Файл    ", command=choose_file)  
btn1.grid(column=1, row=1)  

zad = Label(window, text="Зависимость от:")  
zad.grid(column=1, row=2) 
selected = IntVar()
rad1 = Radiobutton(window, text='длины волны', value=1, variable=selected)  
rad2 = Radiobutton(window, text='частоты', value=2, variable=selected) 
rad1.grid(column=0, row=3)  
rad2.grid(column=2, row=3)  

btn2 = Button(window, text="Построить график", command=clicked, state=DISABLED)  
btn2.grid(column=1, row=5)  
window.mainloop()