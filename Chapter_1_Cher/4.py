import os
from tkinter import *

path = 'C:\\Users\\Админ\\Videos\\Captures\\'


def start(arg):
    os.startfile(path+'BCiW.mp4')


window = Tk()

window.geometry(f"{1000}x{800}")
lbl = Label(window)
lbl.place(x=0, y=0)

window.bind('<Button-1>',start)

window.mainloop()