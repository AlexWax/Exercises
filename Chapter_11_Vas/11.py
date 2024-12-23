from tkinter import *
from time import *


class Snake:
    def __init__(self):
        self.width = 500
        self.height = 400
        self.R = 20

        self.step = 0
        self.speed = 2
        self.speed_x = 0
        self.speed_y = 0
        self.num_proc = []

        self.main()
        self.binds()
        self.vars()
        self.traces()
        self.start()

    def up(self, *args):
        self.text.set('up')

    def down(self, *args):
        self.text.set('dn')

    def left(self, *args):
        self.text.set('lt')

    def right(self, *args):
        self.text.set('rt')

    def motion(self, *args):

        if self.key:
            self.text.trace_vdelete('w', self.a)
            self.key = False

        if self.text.get() == 'lt':
            self.cnv.move(self.crl, -self.speed, 0)
            self.wdw.after(100, self.motion)
        if self.text.get() == 'rt':
            self.cnv.move(self.crl, self.speed, 0)
            self.wdw.after(100, self.motion)
        if self.text.get() == 'up':
            self.cnv.move(self.crl, 0, -self.speed)
            self.wdw.after(100, self.motion)
        if self.text.get() == 'dn':
            self.cnv.move(self.crl, 0, self.speed)
            self.wdw.after(100, self.motion)


    def stop_it(self, *args):
        self.bol.set(True)

    def main(self):
        self.wdw = Tk()
        self.wdw.geometry(f"{self.width}x{self.height}")
        self.cnv = Canvas(self.wdw, bd=3)
        self.cnv.place(x=self.width / 4, y=self.height / 4, width=self.width / 2, height=self.height / 2)
        self.cnv.focus_set()
        self.crl = self.cnv.create_oval(self.width / 4 - self.R, self.height / 4 - self.R, self.width / 4 + self.R, self.height / 4 + self.R, fill='green')

    def vars(self):
        self.text = StringVar()
        self.bol = BooleanVar()
        self.bol.set(True)
        self.bol_up = BooleanVar()
        self.bol_up.set(True)

    def binds(self):
        self.cnv.bind('<Up>', self.up)
        self.cnv.bind('<Down>', self.down)
        self.cnv.bind('<Left>', self.left)
        self.cnv.bind('<Right>', self.right)
        self.cnv.bind('<Motion>', self.motion)
        self.cnv.bind('<Button-1>', self.stop_it)

    def traces(self):
        self.a = self.text.trace('w', self.motion)
        self.key = True

    def start(self):
        self.wdw.mainloop()


Snake()