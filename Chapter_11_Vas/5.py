from tkinter import *


def set_up(*args):
    global fonts
    fonts[1] = fonts[1] + 1
    lbl.configure(font=fonts)


def set_down(*args):
    global fonts
    fonts[1] = fonts[1] - 1
    lbl.configure(font=fonts)


wdw = Tk()
fonts = ['Arial', 10]
text = StringVar()
text.set('Some text')
width = 300
height = 200
wdw.geometry(f"{width}x{height}")

lbl = Label(wdw, textvariable=text)

btn = Button(wdw, text='Clear',  command=set_up)
btn2 = Button(wdw, text='Close',  command=set_down)

lbl.place(x=width/4, y=height/4, width=width/2, height=50)
btn.place(x=width/8, y=2*height/4, width=width/4, height=50)
btn2.place(x=5*width/8, y=2*height/4, width=width/4, height=50)

wdw.mainloop()