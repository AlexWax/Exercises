from tkinter import *
from time import *

def click():
    global t
    t = txt.get()
    sleep(3)
    window.destroy()

window = Tk()
t = ''
a = 1000
b = 750
window.geometry(f"{a}x{b}")

txt = Entry(master=window)
but1 = Button(window, text='Red', command=click)
but2 = Button(window, text='Green', command=window.destroy)

txt.place(x=a/2, y=b/3)
but1.place(x=a/4, y=b/2)
but2.place(x=3*a/4, y=b/2)

window.mainloop()

if t != '':
    window2 = Tk()
    window2.geometry(f"{a}x{b}")
    lbl2 = Label(window2, text=t)
    but21 = Button(window2, text='Ok', command=window2.destroy)

    lbl2.place(x=a/2, y=a/3)
    but21.place(x=a/2, y=b/2)

    window2.mainloop()
