from tkinter import *


def set_all(*args):
    try:
        text2.set(eval(text.get()))
    except SyntaxError:
        text2.set(text2.get())
    except NameError as error:
        text2.set(text2.get() + f'\n Please delete let :{error.name}')


def clear_all(*args):
    text.set('')


wdw = Tk()
text = StringVar()
text2 = StringVar()
width = 500
height = 200
wdw.geometry(f"{width}x{height}")

frame_inp = Frame(wdw, bd=3, relief=GROOVE)
frame_oup = Frame(wdw, bd=3, relief=GROOVE)
frame_inp.place(x=0, y=0, width=width/2, height=height)
frame_oup.place(x=width/2, y=0, width=width/2, height=height)

inp = Entry(frame_inp, textvariable=text)
btn = Button(frame_inp, text='Clear', command=clear_all)
inp.place(x=width/8, y=height/3, width=width/4, height=50)
btn.place(x=width/8, y=2*height/3, width=width/4, height=50)

lbl = Label(frame_oup, textvariable=text2)
btn2 = Button(frame_oup, text='Close', command=wdw.destroy)
lbl.place(x=width/8, y=height/3, width=width/4, height=50)
btn2.place(x=width/8, y=2*height/3, width=width/4, height=50)

text.trace('w', set_all)
wdw.mainloop()
