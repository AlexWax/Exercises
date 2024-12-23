from tkinter import *


def next_img(*args):
    lbl.configure(bg=color.get())


wdw = Tk()
width = 500
height = 400
color = StringVar()
colors = ['red', 'green', 'blue']
wdw.geometry(f"{width}x{height}")

rbs = [Radiobutton(wdw, variable=color, text=clr, value=clr+'2') for clr in colors]
for rb in rbs:
    rb.pack(side='left', padx=5)
color.set(colors[0])

lbl = Label(wdw, bg=color.get())
lbl.place(x=width/2, y=height/4, width=width/2, height=height/2)

color.trace('w', next_img)
wdw.mainloop()