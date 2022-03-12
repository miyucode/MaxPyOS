from System.Shutdown import Shutdown
from System.Restart import Restart

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

import tkinter.messagebox as mb


def Home():
	home = Tk()
	home.title("MaxPyOS - Home")
	home.geometry("720x450")
	home.resizable(False, False)
	home.iconbitmap("UI/Menu/icons/logo.ico")

	def menu():
		def closemenu():
			menu.destroy()
			home.deiconify()

		def restartmaxpyos():
			home.withdraw()
			menu.withdraw()
			asking = mb.askquestion('MaxPyOS - Restart', 'Are you sure to restart ?')
			if asking == "yes":
				home.destroy()
				Restart.restart()
			elif asking == "no":
				menu.deiconify()

		def shutdownmaxpyos():
			home.withdraw()
			menu.withdraw()
			asking = mb.askquestion('MaxPyOS - Shutdown', 'Are you sure to shutdown ?')
			if asking == "yes":
				home.destroy()
				Shutdown.shutdown()
			elif asking == "no":
				menu.deiconify()

		home.withdraw()
		menu = Toplevel()
		menu.geometry("400x400")
		menu.title("MaxPyOS - Select shutdown, restart or cancel.")
		menu.iconbitmap("UI/Menu/icons/logo.ico")
		menu.resizable(False, False)
		menu.protocol("WM_DELETE_WINDOW", lambda: closemenu())
		iconshutdown = PhotoImage(file="UI/Menu/icons/shutdown-icon.png")
		output_iconshutdown = Label(menu, image=iconshutdown)
		output_iconshutdown.image = iconshutdown
		output_iconshutdown.place(relx=0.32, rely=0.25, anchor=CENTER)
		Button(menu, text="Shutdown MaxPyOS", command=shutdownmaxpyos).place(relx=0.40, rely=0.22)

		iconrestart = PhotoImage(file="UI/Menu/icons/restart-icon.png")
		output_iconrestart = Label(menu, image=iconrestart)
		output_iconrestart.image = iconrestart
		output_iconrestart.place(relx=0.32, rely=0.40, anchor=CENTER)
		Button(menu, text="Restart MaxPyOS", command=restartmaxpyos).place(relx=0.42, rely=0.38)

	iconlogotaskbar = PhotoImage(file="UI/Menu/icons/logo-png.png")
	output_iconlogotaskbar = Button(home, image=iconlogotaskbar, command=menu)
	output_iconlogotaskbar.image = iconlogotaskbar
	output_iconlogotaskbar.place(relx=0.05, rely=0.90, anchor=CENTER)