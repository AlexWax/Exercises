import tkinter.ttk
from tkinter import *

def change_img(evt):
    txt = cd.get()
    print(txt)
    if txt in img_name_list:
        lbl.configure(image=imgs[img_name_list.index(txt)])


window = Tk()
a = 750
b = 500
txt = ''
path = "C:\\Users\\Админ\\Pictures\\Saved Pictures\\"
img_name_list = ['A', 'B', 'C']
img_name_real_list = ['SISI.png', 'SISI.png', 'SISI.png']
imgs = [PhotoImage(file=name) for name in img_name_real_list]
window.geometry(f"{a}x{b}")

lbl = Label(window, image=imgs[0])
lbl.place(x=10, y=10)

cd = tkinter.ttk.Combobox(window, state='readonly', values=img_name_list)
cd.current(0)
cd.bind("<<ComboboxSelected>>", change_img)
cd.place(x=a/2, y=b/2)

btn = Button(window, text='Ok', command=window.destroy)
btn.place(x=a/2, y=b/2)

window.mainloop()


