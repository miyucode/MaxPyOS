from tkinter import *
from tkinterweb import HtmlFrame
from tkinter.ttk import *

import tkinter.messagebox as mb
import os

def maxweb():
    app = Tk()
    app.geometry(f"800x500")
    app.resizable(False, False)
    app.iconbitmap("Apps/MaxWeb/icons/maxweb-icon.ico")
    app.title("MaxWeb - Home")
    
    frame = HtmlFrame(app, messages_enabled=False)
    frame.load_website("duckduckgo.com")
    frame.pack(fill="both", expand=True)

    def searchurl():
        url = url_entry.get()
        frame.load_website(url)
        url_entry.delete(0, "end")
        app.title(f"MaxWeb - {url}")
        tabname.config(text=url)

    def url_changed(title):
        tabname.config(text=title)
        
    frame.on_url_change(url_changed)
    frame.set_broken_webpage_message("<h1><br><br>Oops, we can't reach this URL, retry. :)</h1>")

    url_entry = Entry(app)
    url_entry.place(relx=0.01, rely=0.01)
    url_entry.insert(0, "")

    tabname = Label(app, text="https://duckduckgo.com", font=("Monospace", 15))
    tabname.place(relx=0.60, rely=0.01)

    Button(app, text="Search", command=searchurl).place(relx=0.18, rely=0.005)

    app.mainloop()