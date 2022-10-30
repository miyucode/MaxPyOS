from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from UI.Menu import menu

from pygame import mixer

import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os

def musicplayer():
    app = Tk()
    app.title("MaxPyOS - Music Player")
    app.geometry("650x400")
    app.resizable(False, False)
    app.protocol("WM_DELETE_WINDOW", lambda: [stopmusic(), app.destroy()])
    app.iconbitmap("Apps/MusicPlayer/icons/music-icon.ico")
    
    def readaudio():
        app.withdraw()
        startmusicbtn.place_forget()
        mixer.init()

        def raudio():
            mixer.music.load(file)
            mixer.music.play()

            app.deiconify()
            app.title(f"MaxPyOS - Music Player ({file})")
            music_name.config(text=f"Listening: {file}")
            pausebtn1.place(relx=0.45, rely=0.80)
            stopbtn.place(relx=0.30, rely=0.80)

        file = filedialog.askopenfilename(defaultextension='*.mp3*', title="Select a music", initialdir=f"C:/Users/{os.getlogin()}/Desktop", filetypes=[('MP3', '*.mp3*'), ("WAW", "*.waw*")])
        if file == "":
            mb.showerror("Music Player - Error", "You have selected no files!")
            startmusicbtn.place(relx=0.35, rely=0.10)
            app.deiconify()
        else:
            raudio()

    def stopmusic():
        try:
            mixer.music.stop()
            pausebtn1.place_forget()
            pausebtn2.place_forget()
            stopbtn.place_forget()
            startmusicbtn.place(relx=0.35, rely=0.10)
            music_name.config(text="Listening:")
        except:
            pass

    def pausemusic1():
        mixer.music.pause()
        pausebtn1.place_forget()
        pausebtn2.place(relx=0.45, rely=0.80)

    def pausemusic2():
        mixer.music.unpause()
        pausebtn1.place(relx=0.45, rely=0.80)
        pausebtn2.place_forget()

    iconmusic = PhotoImage(master=app, file="UI/Menu/icons/music-icon.png")
    output_iconmusic = Label(app, text="music icon", image=iconmusic)
    output_iconmusic.image = iconmusic
    output_iconmusic.place(relx=0.05, rely=0.06, anchor=CENTER)
    Label(app, text="MusicPlayer", font=("Segoe UI", 15, "bold")).place(relx=0.09, rely=0.02)

    startmusicbtn = Button(app, text="Choose a music (MP3, WAW)", command=readaudio)

    iconstopmusic = PhotoImage(master=app, file="Apps/MusicPlayer/icons/stopmusic-icon.png")
    stopbtn = Button(app, text="Stop", command=stopmusic, image=iconstopmusic)
    stopbtn.image = iconstopmusic

    iconpausebtn1 = PhotoImage(master=app, file="Apps/MusicPlayer/icons/pause-icon.png")
    pausebtn1 = Button(app, text="Pause", command=pausemusic1, image=iconpausebtn1)
    pausebtn1.image = iconpausebtn1
    
    iconpausebtn2 = PhotoImage(master=app, file="Apps/MusicPlayer/icons/playmusic-icon.png")
    pausebtn2 = Button(app, text="Unpause", command=pausemusic2, image=iconpausebtn2)
    pausebtn2.image = iconpausebtn2

    music_name = Label(app, text="Listening: ", font=("Segoe UI", 16, "bold"))
    music_name.place(relx=0.05, rely=0.70)

    pausebtn1.place_forget()
    pausebtn2.place_forget()
    stopbtn.place_forget()
    startmusicbtn.place(relx=0.40, rely=0.10)

    app.mainloop()
