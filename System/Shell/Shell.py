from UI.Menu import menu

import tkinter.messagebox as mb
import time
import os

def shell():
	while True:
		i = input("Admin >> ")
		if i == "close":
			break
		elif i == "check":
			print("Admin >> Checking...")
			print("Admin >> Check finished !")
		else:
			print("Admin >> This command does not exist !")