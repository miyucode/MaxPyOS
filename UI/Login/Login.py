from UI.Menu.menu import Home

from tkinter import *
from tkinter.ttk import *
from time import *
from tkinter import ttk

import tkinter.messagebox as mb

def login():
	def cancelLogin():
		Login.withdraw()
		mb.showinfo("MaxPyOS","Click on OK for cancel login.")
		print(f"[{strftime('%H:%M:%S')}]: Login has been cancel with success.")
		Login.destroy()

	def ConnectionToAccount():
		password = open('System/Ressources/password.txt', 'r')
		Password = password.read()
		password.close()
		contentofinput = passwordinput.get()
		Login.withdraw()
		if len(contentofinput) > 0:
			if contentofinput == Password:
				Login.destroy()
				print(f"[{strftime('%H:%M:%S')}]: Login has been done with success.")
				Home()
			else:
				mb.showerror("MaxPyOS","Incorrect Password !")
				Login.deiconify()
		else:
			mb.showerror("MaxPyOS","Incorrect Password !")
			Login.deiconify()

	Login = Tk()
	Login.title("MaxPyOS - Login")
	Login.geometry("600x400")
	Login.resizable(False, False)
	Login.iconbitmap("UI/Login/icons/login.ico")
	Login.protocol("WM_DELETE_WINDOW", lambda: cancelLogin())

	iconusername = PhotoImage(file="UI/Login/icons/usericon.png")
	output_iconusername = Label(Login, image=iconusername)
	output_iconusername.image = iconusername
	output_iconusername.place(relx=0.40, rely=0.15, anchor=CENTER)
	Label(Login, text="Admin", font=("Arial", 15)).place(relx=0.50, rely=0.15, anchor=CENTER)

	iconpassword = PhotoImage(file="UI/Login/icons/passwordicon.png")
	output_iconpassword = Label(Login, image=iconpassword)
	output_iconpassword.image = iconpassword
	output_iconpassword.place(relx=0.25, rely=0.25, anchor=CENTER)
	passwordinput = Entry(Login, text="password here.", font=("Arial", 15))
	passwordinput.place(relx=0.50, rely=0.25, anchor=CENTER)

	ConnectButton = Button(Login, text="Login", command=ConnectionToAccount, width=30) 
	ConnectButton.place(relx=0.5, rely=0.50, anchor=CENTER)

	Login.mainloop()
