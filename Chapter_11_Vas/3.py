import datetime
import time
from tkinter import *
from time import *

class YourAge:
    def __init__(self):
        self.main()

    def click(self, *args):
        try:
            self.born_date = datetime.date(int(self.npt_year.get()), int(self.npt_month.get()), int(self.npt_day.get()))
            self.wdw.destroy()
            self.answer()
        except TypeError as error:
            self.error()
            self.wdw.destroy()
            self.wdw_error.mainloop()

    def close(self):
        self.wdw_error.destroy()
        self.main()


    def main(self):
        self.wdw = Tk()
        self.wdw.geometry(f"{200}x{200}")

        year = Frame(self.wdw, bd=3, relief=GROOVE)
        month = Frame(self.wdw, bd=3, relief=GROOVE)
        day = Frame(self.wdw, bd=3, relief=GROOVE)

        year.pack(side='top', fill='both')
        lbl_year = Label(year, text='Year?')
        self.npt_year = Entry(year)
        lbl_year.pack(side='top', fill='both')
        self.npt_year.pack(side='top', fill='both')

        month.pack(side='top', fill='both')
        lbl_month = Label(month, text='Month?')
        self.npt_month = Entry(month)
        lbl_month.pack(side='top', fill='both')
        self.npt_month.pack(side='top', fill='both')

        day.pack(side='top', fill='both')
        lbl_day = Label(day, text='Day?')
        self.npt_day = Entry(day)
        lbl_day.pack(side='top', fill='both')
        self.npt_day.pack(side='top', fill='both')

        btn = Button(self.wdw, text='Confirm', relief=GROOVE, command=self.click)
        btn.pack(side='bottom', fill='both')

        self.wdw.mainloop()

    def answer(self):
        wdw2 = Tk()
        wdw2.geometry(f"{200}x{200}")
        time_del = datetime.date.today() - self.born_date
        lbl = Label(wdw2, text=str(time_del))
        lbl.pack(side='top', fill='both')

        wdw2.mainloop()

    def error(self):
        self.wdw_error = Tk()
        self.wdw_error.geometry(f"{200}x{200}")

        lbl_error = Label(self.wdw_error, text='Not correct data format! \n Use numbers')
        lbl_error.pack(side='top', fill='both')

        btn_error = Button(self.wdw_error, text='Ok', command=self.close)
        btn_error.pack(side='top', fill='both')


YourAge()