from System.Shutdown import Shutdown
from System.Restart import Restart
from UI.Login import Login

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from time import strftime

import tkinter.messagebox as mb

def Home():
	def Settings():
		def closeSettings():
			settings.destroy()
			home.deiconify()

		home.withdraw()
		settings = Toplevel()
		settings.title("MaxPyOS - Settings")
		settings.geometry("600x500")
		settings.resizable(False, False)
		settings.iconbitmap("UI/Menu/icons/options-icon.ico")
		settings.protocol("WM_DELETE_WINDOW", lambda: closeSettings())

	home = Tk()
	home.title("MaxPyOS - Home")
	home.geometry("720x450")
	home.resizable(False, False)
	home.iconbitmap("UI/Menu/icons/logo.ico")

	def menu():
		def disconnectaccount():
			home.destroy()
			print(f"[{strftime('%H:%M:%S')}]: Disconnected with success.")
			Login.login()
			print(f"[{strftime('%H:%M:%S')}]: Starting...")

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
		menu.title("MaxPyOS - Home")
		menu.iconbitmap("UI/Menu/icons/logo.ico")
		menu.resizable(False, False)
		menu.protocol("WM_DELETE_WINDOW", lambda: closemenu())
		iconshutdown = PhotoImage(file="UI/Menu/icons/shutdown-icon.png")
		output_iconshutdown = Label(menu, image=iconshutdown)
		output_iconshutdown.image = iconshutdown
		output_iconshutdown.place(relx=0.32, rely=0.25, anchor=CENTER)
		Button(menu, text="Shutdown MaxPyOS", command=shutdownmaxpyos).place(relx=0.40, rely=0.23)

		iconrestart = PhotoImage(file="UI/Menu/icons/restart-icon.png")
		output_iconrestart = Label(menu, image=iconrestart)
		output_iconrestart.image = iconrestart
		output_iconrestart.place(relx=0.32, rely=0.40, anchor=CENTER)
		Button(menu, text="Restart MaxPyOS", command=restartmaxpyos).place(relx=0.40, rely=0.38)

		icondisconnect = PhotoImage(file="UI/Menu/icons/disconnect-icon.png")
		output_icondisconnect = Label(menu, image=icondisconnect)
		output_icondisconnect.image = icondisconnect
		output_icondisconnect.place(relx=0.32, rely=0.55, anchor=CENTER)
		Button(menu, text="Disconnect", command=disconnectaccount).place(relx=0.40, rely=0.53)

	iconlogotaskbar = PhotoImage(file="UI/Menu/icons/logo-png.png")
	output_iconlogotaskbar = Button(home, image=iconlogotaskbar, command=menu)
	output_iconlogotaskbar.image = iconlogotaskbar
	output_iconlogotaskbar.place(relx=0.05, rely=0.90, anchor=CENTER)

	iconoptions = PhotoImage(file="UI/Menu/icons/options-icon.png")
	output_iconoptions = Button(home, text="Settings",image=iconoptions, command=Settings)
	output_iconoptions.image = iconoptions
	output_iconoptions.place(relx=0.15, rely=0.90, anchor=CENTER)