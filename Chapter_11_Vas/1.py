from tkinter import *
from time import *
"""Cursor interaction"""


def curs_on(*args):
    sleep(0.3)
    cnv.itemconfig(pct, image=img_2)


def curs_off(*args):
    sleep(0.3)
    cnv.itemconfig(pct, image=img_1)


"""Main body"""
wdw = Tk()
wdw.geometry(f"{400}x{400}")
cnv = Canvas(wdw, bd=3, relief=GROOVE)
cnv.pack(side='left', fill='both', padx=10, pady=10)
cnv.focus_set()

img_1 = PhotoImage(file='SISI.png')
img_2 = PhotoImage(file='NOJKI.png')
pct = cnv.create_image(200, 200, anchor='center', image=img_1)

cnv.bind('<Enter>', curs_on)
cnv.bind('<Leave>', curs_off)

btn = Button(wdw, text='Close', command=wdw.destroy)
btn.pack(side='top', fill='none')

wdw.mainloop()