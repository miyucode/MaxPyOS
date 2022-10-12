from tkinter import *

import tkinter.messagebox as mb
import os

def covidapp():
    app = Tk()
    app.geometry(f"800x500")
    app.iconbitmap("Apps/CovidApp/icons/coronavirus-icon.ico")
    app.title("CovidApp")

    iconlatestcases = PhotoImage(master=app, file="Apps/CovidApp/icons/coronavirus-iconpng.png")
    output_iconlatestcases = Label(app, text="latest cases icon", image=iconlatestcases)
    output_iconlatestcases.image = iconlatestcases
    output_iconlatestcases.place(relx=0.05, rely=0.10, anchor=CENTER)

    
    
    app.mainloop()