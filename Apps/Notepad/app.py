from UI.Menu import menu

from tkinter import *
from tkinter.scrolledtext import ScrolledText

import tkinter.filedialog as fd
import tkinter.messagebox as mb

import platform
import os
import sys

def notepad():
	filepath = ""

	def setfilepath(path):
		global filepath
		filepath = path

	def openfile():
		path = fd.askopenfilename()
		if path == "":
			mb.showerror("Notepad","Vous n'avez sélectionné aucun fichier texte !")
		else:
			with open(path, 'r') as f:
				code = f.read()
				editor.delete('1.0', END)
				editor.insert("1.0", code)
				setfilepath(path)
				root.wm_title("Notepad - " + filepath)

	def savefile():
		if filepath == "":
			mb.showerror("Notepad","Vous n'avez aucun nom à votre fichier texte !")
		else:
			with open(filepath, 'w') as f:
				code = editor.get('1.0', END)
				f.write(code)
				setfilepath(filepath)
				root.wm_title("Notepad - " + filepath)

	def saveasfile():
		path = fd.asksaveasfilename()
		if path == "":
			mb.showerror("Notepad","Vous n'avez aucun nom à votre fichier texte !")
		else:
			with open(path, 'w') as f:
				code = editor.get('1.0', END)
				f.write(code)
				setfilepath(path)
				root.wm_title("Notepad - " + filepath)

	root = Tk()
	root.wm_title("Notepad - Blank")
	root.geometry("400x400")
	root.resizable(False, False)
	root.iconbitmap("Apps/Notepad/icons/notepad-icon.ico")
	editor = ScrolledText(root, wrap=WORD, undo=True)
	editor.pack(fill=BOTH, expand=True)
	menubar = Menu(root)
	fileMenu = Menu(menubar, tearoff=0)
	fileMenu.add_command(label="Open", command=openfile)
	fileMenu.add_command(label="Save", command=savefile, accelerator="Ctrl+S")
	fileMenu.add_command(label="Save As", command=saveasfile)
	fileMenu.add_separator()
	fileMenu.add_command(label="Close", command=root.destroy)
	editMenu = Menu(menubar, tearoff=False)
	editMenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: editor.event_generate('<<Cut>>'))
	editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: editor.event_generate('<<Copy>>'))
	editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: editor.event_generate('<<Paste>>'))
	editMenu.add_separator()
	editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=editor.edit_undo)
	editMenu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", command=editor.edit_redo)
	menubar.add_cascade(label="File", menu=fileMenu)
	menubar.add_cascade(label="Edit", menu=editMenu)
	root.config(menu=menubar)
	root.bind()
	root.mainloop()