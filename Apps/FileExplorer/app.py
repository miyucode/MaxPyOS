from UI.Menu import menu

from tkinter import *
from tkinter.scrolledtext import ScrolledText

from Apps.Notepad.app import notepad, openFile

import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os

def fileexplorer():
	app = Tk()
	app.title("MaxPyOS - File Explorer")
	app.geometry("800x500")
	app.resizable(False, False)
	app.iconbitmap("Apps/FileExplorer/icons/fileexplorer-icon.ico")

	def delete_folder():
		dir_to_delete = fd.askdirectory(title="Which folder to delete?", initialdir="System/Users/User/Desktop")
		if dir_to_delete == "":
			mb.showerror(title="Error!", message="We\'re not enable to delete this folder !")
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1
		else:
			os.rmdir(dir_to_delete)
			mb.showinfo('MaxPyOS - File Explorer','Folder has been deleted with success.')
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1

	def updatelist():
		i = 0
		files = os.listdir("System/Users/User/Desktop/")
		listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
		listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
		scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
		scrollbar.pack(side=RIGHT, fill=Y)
		listbox.config(yscrollcommand=scrollbar.set)
		while i < len(files):
			listbox.insert(END, files[i])
			i += 1

	def copy_file():
		file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")], initialdir="System/Users/User/Desktop")
		dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?", initialdir="System/Users/User/Desktop")
		if file_to_copy == "":
			mb.showerror(title="Error!", message='We\'re not enable to copy this file !')
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1
		else:
			if dir_to_copy_to == "":
				mb.showerror(title="Error!", message='We\'re not enable to copy this file !')
				i = 0
				files = os.listdir("System/Users/User/Desktop/")
				listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
				listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
				scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
				scrollbar.pack(side=RIGHT, fill=Y)
				listbox.config(yscrollcommand=scrollbar.set)
				while i < len(files):
					listbox.insert(END, files[i])
					i += 1
			else:
				try:
					shutil.copy(file_to_copy, dir_to_copy_to)
					mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
					i = 0
					files = os.listdir("System/Users/User/Desktop/")
					listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
					listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
					scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
					scrollbar.pack(side=RIGHT, fill=Y)
					listbox.config(yscrollcommand=scrollbar.set)
					while i < len(files):
						listbox.insert(END, files[i])
						i += 1
				except:
					mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')
					i = 0
					files = os.listdir("System/Users/User/Desktop/")
					listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
					listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
					scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
					scrollbar.pack(side=RIGHT, fill=Y)
					listbox.config(yscrollcommand=scrollbar.set)
					while i < len(files):
						listbox.insert(END, files[i])
						i += 1
	
	def delete_file():
		file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")], initialdir="System/Users/User/Desktop")
		if file == "":
			mb.showerror(title="Error!", message='We\'re not enable to delete this file !')
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1
		else:
			os.remove(os.path.abspath(file))
			mb.showinfo('MaxPyOS - File Explorer', message='File has been deleted with success.')
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1

	def open_file():
		file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.*")], initialdir="System/Users/User/Desktop")
		if file == "":
			mb.showerror(title="Error!", message='We\'re not enable to open this file !')
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1
		else:
			i = 0
			files = os.listdir("System/Users/User/Desktop/")
			listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
			listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
			scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
			scrollbar.pack(side=RIGHT, fill=Y)
			listbox.config(yscrollcommand=scrollbar.set)
			while i < len(files):
				listbox.insert(END, files[i])
				i += 1
			split_file = os.path.splitext(file)
			file_extension = split_file[1]
			if file_extension == ".txt":
				openFile(file)
			else:
				os.startfile(os.path.abspath(file))

	def list_files_in_folder():
		i = 0
		files = os.listdir("System/Users/User/Desktop/")
		listbox = Listbox(app, selectbackground='SteelBlue', font=("Arial", 10))
		listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
		scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
		scrollbar.pack(side=RIGHT, fill=Y)
		listbox.config(yscrollcommand=scrollbar.set)
		while i < len(files):
			listbox.insert(END, files[i])
			i += 1

	list_files_in_folder()

	menubar = Menu(app)

	file = Menu(menubar, tearoff=0)
	file.add_command(label="Open a file", command=open_file)
	file.add_command(label="Delete a file", command=delete_file)
	file.add_command(label="Copy a file", command=copy_file)
	file.add_separator()
	file.add_command(label="Delete a folder", command=delete_folder)
	file.add_separator()
	file.add_command(label="Update", command=updatelist)

	menubar.add_cascade(label="File", menu=file)

	app.config(menu=menubar)
	app.mainloop()