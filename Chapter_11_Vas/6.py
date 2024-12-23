from tkinter import *


def next_img(*args):
    lbl.configure(image=imgs[lst.curselection()[0]])


wdw = Tk()
width = 500
height = 400
img_names = ['NOJKI', 'SISI']
wdw.geometry(f"{width}x{height}")

lst = Listbox(wdw, selectmode=SINGLE, height=len(img_names), bg='white', selectbackground='grey')
lst.place(x=width/8, y=3*height/8, width=width/4)
for name in img_names:
    lst.insert(END, name)
lst.select_set(0)
lst.bind('<<ListboxSelect>>', next_img)

imgs = [PhotoImage(file=name+'.png') for name in img_names]
lbl = Label(wdw, image=imgs[lst.curselection()[0]])
lbl.place(x=width/2, y=height/4, width=width/2, height=height/2)

wdw.mainloop()