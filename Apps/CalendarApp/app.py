from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from tkcalendar import *

import tkinter.messagebox as mb

import datetime

def calendarapp():
    calendarapp = Tk()
    calendarapp.title("MaxPyOS - Calendar")
    calendarapp.geometry("350x220")
    calendarapp.minsize(300, 350)
    calendarapp.maxsize(350, 250)
    calendarapp.iconbitmap("Apps/CalendarApp/icons/calendar-icon.ico")

    current_day = datetime.date.today().day
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year

    cal = Calendar(calendarapp, selectmode="day", year=current_year, month=current_month, day=current_day)
    cal.pack(pady=20)

    Label(calendarapp, text=f"Today is the {current_month}/{current_day}/{current_year} !", font=("Monospace", 14)).pack(pady=20)
    Label(calendarapp, text="Last event: 9/8/2022, \nDeath of Elizabeth II. Rest in Peace !", font=("Monospace", 15)).pack()

    calendarapp.mainloop()