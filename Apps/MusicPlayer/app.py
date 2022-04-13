from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from UI.Menu import menu

from pygame import mixer

import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os

def musicplayer():
	def readaudio():
		a = 1

	def stopmusic():
		try:
			mixer.music.stop()
		except:
			pass
		musicplayer.destroy()

	musicplayer = Tk()
	musicplayer.title("MaxPyOS - Music Player")
	musicplayer.geometry("500x400")
	musicplayer.resizable(False, False)
	musicplayer.protocol("WM_DELETE_WINDOW", lambda: stopmusic())
	musicplayer.iconbitmap("Apps/MusicPlayer/icons/music-icon.ico")
	iconoptions = PhotoImage(file="Apps/MusicPlayer/icons/playmusic-icon.png")
	
	musicplayer.mainloop()
