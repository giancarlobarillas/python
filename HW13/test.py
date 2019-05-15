from tkinter import *


def say_hello():
    name = entry1.get()
    label2 = Label(window, text=name)
    label2.grid(row=1, column=1)


window = Tk()

label1 = Label(window, text="Please enter name")
entry1 = Entry(window)
button1 = Button(window, text="Click ME", command=say_hello)

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=1, column=0)

window.mainloop()
