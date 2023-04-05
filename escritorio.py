from tkinter import *
from tkinter import messagebox

def saludar():
    print("Hola " + txt_nombre.get())
    messagebox.showinfo("mensaje","Hola" + txt_nombre.get())

app = Tk()
app.geometry('300x100')
app.title('Mi primera app')

lb_nombre = Label(app, text='Nombre : ')
lb_nombre.grid(row=0, column=0)

txt_nombre = Entry(app)
txt_nombre.grid(row=0,column=1)

btn_saludo = Button(app, text='Saludar', command=saludar)
btn_saludo.grid(row=0,column=2)

app.mainloop()