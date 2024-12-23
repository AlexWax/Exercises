from tkinter import *

"""Functions"""

def get_font():
    res = []
    name = lst.get(lst.curselection())
    size = scl.get()

    res.append(name)
    res.append(size)

    if bold.get() != '':
        res.append(bold.get())
    if italic.get() != '':
        res.append(italic.get())
    return res


def set_all(*args):
    fnt = get_font()
    lbl.configure(font=fnt, fg=color.get())
    txt = '>' * fnt[1]

    text.set(text.get())

"""Variables"""
fnt_1 = ['Arial', 12, 'italic']
fnt_2 = ['Times New Roman', 13, 'bold', 'italic']
fonts = ['Times New Roman', 'Arial', 'Courier New']
font_min_size = 10
font_max_size = 20
"""Window"""
window = Tk()
a = 750
b = 500
window.title('AGA')
window.geometry(f"{a}x{b}")
"""Frames"""
frm_scale = Frame(window, bd=3, relief=GROOVE)
frm_text = Frame(window, bd=3, relief=GROOVE)
frm_btn = Frame(window, bd=3, relief=GROOVE)
frm_lich = Frame(window, bd=3, relief=GROOVE)
frm_list = Frame(frm_lich, bd=3, relief=GROOVE)
frm_check = Frame(frm_lich, bd=3, relief=GROOVE)

text = StringVar()
color = StringVar()
bold = StringVar()
italic = StringVar()
"""Labels"""
lbl_txt = Label(frm_text, text='Text Ex')
lbl_color = Label(frm_scale, text='Color')
lbl_size = Label(frm_scale, text='Size')
lbl_font = Label(frm_list, text='Font')
lbl_style = Label(frm_check, text='Style')

lbl = Label(frm_text, textvariable=text)
lbl.configure(bg='white', relief=RAISED)
"""Switcher"""
rb_1 = Radiobutton(frm_scale, text='красный',
                   variable=color, value='red')
rb_2 = Radiobutton(frm_scale, text='синий',
                   variable=color, value='blue')
rb_3 = Radiobutton(frm_scale, text='черный',
                   variable=color, value='black')
color.set('blue')
"""Slider"""
scl = Scale(frm_scale, orient=HORIZONTAL,
            tickinterval=2, resolution=1,
            from_=font_min_size, to=font_max_size)
scl.config(command=set_all)
"""CheckButton"""
cb_1 = Checkbutton(frm_check, text='жир',
                   variable=bold, onvalue='bold',
                   offvalue='')
cb_2 = Checkbutton(frm_check, text='курсив',
                   variable=italic, onvalue='italic',
                   offvalue='')
bold.set('')
italic.set('italic')
"""StaticList"""
lst = Listbox(frm_list, selectmode=SINGLE, font=fnt_1, bg='grey96',
              selectbackground='gray', height=len(fonts))
for n in fonts:
    lst.insert(END, n)
lst.select_set(0)
lst.bind('<<ListboxSelect>>', set_all)
"""Button"""
btn = Button(frm_btn, text='OK', font=fnt_2,
             command=window.destroy)
"""Position"""
frm_text.pack(side='top', fill='both', padx=5, pady=5)
lbl_txt.pack(side='top', fill='both', padx=5, pady=5)
lbl.pack(side='top', fill='both', padx=5, pady=5)

frm_lich.pack(side='left', fill='both', padx=5, pady=5)

frm_list.pack(side='top', fill='both', padx=5, pady=5)
frm_check.pack(side='top', fill='both', padx=5, pady=5)
lbl_font.pack(side='top', fill='both', padx=5, pady=5)
lst.pack(side='top', fill='both', padx=5, pady=5)

lbl_style.pack(side='top', fill='both', padx=5, pady=5)
cb_1.pack(side='left', fill='both', padx=5, pady=5)
cb_2.pack(side='left', fill='both', padx=5, pady=5)

frm_scale.pack(side='top', fill='both', padx=5, pady=5)
lbl_color.pack(side='top', fill='both', padx=5, pady=5)
lbl_size.pack(side='bottom', fill='both', padx=5, pady=5)
scl.pack(side='bottom', fill='both', padx=5, pady=5)
rb_1.pack(side='left', fill='both', padx=5, pady=5)
rb_2.pack(side='left', fill='both', padx=5, pady=5)
rb_3.pack(side='left', fill='both', padx=5, pady=5)

frm_btn.pack(side='bottom', fill='both', padx=5, pady=5)
btn.pack(side='top', fill='y', padx=5, pady=5)

set_all()
color.trace('w', set_all)
bold.trace('w', set_all)
italic.trace('w', set_all)
window.mainloop()