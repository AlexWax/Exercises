from tkinter import *


class MyApp:
    def __init__(self):
        self.vars()
        self.main_wdw()
        self.main_menu()
        self.fram()
        self.applt()
        self.traces()
        self.show_main_menu()

    def vars(self):
        self.width = 800
        self.height = 600
        self.animal_list = ['', 'DA', 'Aga']
        self.imgs = ['SISI.png', 'NOJKI.png']

    def main_wdw(self):
        self.wdw = Tk()
        self.wdw.geometry(f"{ self.width}x{ self.height}")

    def show_main_menu(self):
        self.wdw.mainloop()

    def main_menu(self):
        menu = Menu(self.wdw)
        mlist = Menu(self.wdw)
        self.set_mlist(mlist)

        menu.add_cascade(label='Ans', menu=mlist)
        self.wdw.config(menu=menu)

    def fram(self):
        self.photos = [PhotoImage(file=name) for name in self.imgs]
        self.frame = Frame(self.wdw)
        self.frame.place(x=self.width/4, y=3*self.width/16, width=self.width/2, height=self.height/2)
        self.lbl = Label(self.frame, text='NAUKA?', font=30)
        self.lbl.place(x=0, y=0, width=self.width/2, height=self.height/2)

    def set_mlist(self, menu):
        self.name = StringVar()
        for name in self.animal_list:
            menu.add_radiobutton(label=name, value=name, variable=self.name)
        self.name.set(self.animal_list[0])

    def applt(self, *args):
        name = self.name.get()
        if name == '':
            self.lbl.configure(image='', text='Nauka?')
        else:
            self.lbl.configure(image=self.photos[self.animal_list.index(name)-1])


    def traces(self):
        self.name.trace('w', self.applt)

MyApp()