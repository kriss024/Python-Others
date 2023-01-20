from tkinter import *
from tkinter import Menu
from tkinter import messagebox

window = Tk()
window.title("Welcome to Tkinter!")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.focus()
txt.grid(column=1, row=0)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)


selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

def clicked():
   print(selected.get())

btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
btn.grid(column=3, row=1)

def clicked():
    messagebox.showinfo('Message title', 'Message content')

btn = Button(window,text='Click here', bg="orange", fg="red", command=clicked)
btn.grid(column=0,row=2)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

window.mainloop()