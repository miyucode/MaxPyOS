from System.Shutdown import Shutdown
from System.Restart import Restart
from System.Utilities import RaiseError

from UI.Login import Login

from Apps.Notepad.app import notepad
from Apps.WeatherApp.app import weatherapp
from Apps.FileExplorer.app import fileexplorer
from Apps.MusicPlayer.app import musicplayer

from tkinter import *
from tkinter.ttk import *

from time import strftime

from sys import platform
import platform

import tkinter.messagebox as mb

windows = platform == "win32"

def Home():
    def MoreApps():
        def openFileExplorerViaMoreApps():
            moreapps.destroy()
            fileexplorer()

        def openNotepadViaMoreApps():
            moreapps.destroy()
            notepad("")

        def openSettingsViaMoreApps():
            moreapps.destroy()
            Settings()

        def openWeatherAppViaMoreApps():
            moreapps.destroy()
            weatherapp()

        moreapps = Toplevel()
        moreapps.title("MaxPyOS - Apps")
        moreapps.geometry("600x500")
        moreapps.resizable(False, False)
        moreapps.iconbitmap("UI/Menu/icons/menucircled-icon.ico")

        iconoptions = PhotoImage(file="UI/Menu/icons/options-icon.png")
        output_iconoptions = Button(moreapps, text="Settings", image=iconoptions, command=openSettingsViaMoreApps)
        output_iconoptions.image = iconoptions
        output_iconoptions.place(relx=0.15, rely=0.15, anchor=CENTER)
        Label(moreapps, text="Settings", font=("Arial", 10)).place(relx=0.11, rely=0.22)

        iconfileexplorer = PhotoImage(file="UI/Menu/icons/fileexplorer-icon.png")
        output_iconfileexplorer = Button(moreapps, text="FileExplorer", image=iconfileexplorer, command=openFileExplorerViaMoreApps)
        output_iconfileexplorer.image = iconfileexplorer
        output_iconfileexplorer.place(relx=0.30, rely=0.15, anchor=CENTER)
        Label(moreapps, text="File Explorer", font=("Arial", 10)).place(relx=0.24, rely=0.22)

        iconnotepad = PhotoImage(file="UI/Menu/icons/notepad-icon.png")
        output_iconnotepad = Button(moreapps, text="Notepad", image=iconnotepad, command=openNotepadViaMoreApps)
        output_iconnotepad.image = iconnotepad
        output_iconnotepad.place(relx=0.45, rely=0.15, anchor=CENTER)
        Label(moreapps, text="Notepad", font=("Arial", 10)).place(relx=0.405, rely=0.22)

        iconweatherapp = PhotoImage(file="UI/Menu/icons/weatherapp-icon.png")
        output_iconweatherapp = Button(moreapps, text="WeatherApp", image=iconweatherapp, command=openWeatherAppViaMoreApps)
        output_iconweatherapp.image = iconweatherapp
        output_iconweatherapp.place(relx=0.60, rely=0.15, anchor=CENTER)
        Label(moreapps, text="Weather App", font=("Arial", 10)).place(relx=0.53, rely=0.22)

    def Notepad():
        notepad()

    def Settings():

        password = open('System/Ressources/password.txt', 'r')
        output_password = password.read()
        password.close()

        username = open('System/Ressources/username.txt', 'r')
        output_username = username.read()
        username.close()

        def changeUsername():
            username_file = open('System/Ressources/username.txt')
            currentusername = username_file.read()
            username_file.close()

            def confirmChangeUsername():
                newUsername = newusername.get()
                changeUsernameWindow.destroy()

                username = open('System/Ressources/username.txt', 'w')
                username.write(newUsername)
                username.close()

                mb.showinfo("MaxPyOS - Change username","Username has been changed with success.")
                Settings()

            def cancelChangeUsername():
                changeUsernameWindow.destroy()
                Settings()

            settings.destroy()
            changeUsernameWindow = Toplevel()
            changeUsernameWindow.title("MaxPyOS - Change username")
            changeUsernameWindow.geometry("350x300")
            changeUsernameWindow.resizable(False, False)
            changeUsernameWindow.iconbitmap("UI/Menu/icons/usericon.ico")
            changeUsernameWindow.protocol("WM_DELETE_WINDOW", lambda: cancelChangeUsername())

            iconusername = PhotoImage(file="UI/Menu/icons/usericon.png")
            output_iconusername = Label(changeUsernameWindow, image=iconusername)
            output_iconusername.image = iconusername
            output_iconusername.place(relx=0.25, rely=0.15, anchor=CENTER)
            newusername = Entry(changeUsernameWindow, font=("Arial", 12))
            newusername.place(relx=0.25, rely=0.33)
            currentusername = Label(changeUsernameWindow, text=f"Current username: {currentusername}", font=("Arial", 12))
            currentusername.place(relx=0.33, rely=0.14)
            Label(changeUsernameWindow, text="New username:", font=("Arial", 12)).place(relx=0.35, rely=0.24)
            Button(changeUsernameWindow, text="Change username", command=confirmChangeUsername).place(relx=0.37, rely=0.43)

        def changePassword():
            def confirmChangePassword():
                newPassword = passwordinput.get()
                changePasswordWindow.destroy()

                password = open('System/Ressources/password.txt', 'w')
                password.write(newPassword)
                password.close()

                mb.showinfo("MaxPyOS - Change password","Password has been changed with success.")
                Settings()

            def cancelChangePassword():
                changePasswordWindow.destroy()
                Settings()

            settings.destroy()
            changePasswordWindow = Toplevel()
            changePasswordWindow.title("MaxPyOS - Change password")
            changePasswordWindow.geometry("350x300")
            changePasswordWindow.resizable(False, False)
            changePasswordWindow.iconbitmap("UI/Menu/icons/options-icon.ico")
            changePasswordWindow.protocol("WM_DELETE_WINDOW", lambda: cancelChangePassword())

            iconpassword = PhotoImage(file="UI/Login/icons/passwordicon.png")
            output_iconpassword = Label(changePasswordWindow, image=iconpassword)
            output_iconpassword.image = iconpassword
            output_iconpassword.place(relx=0.25, rely=0.15, anchor=CENTER)

            currentpassword = Label(changePasswordWindow, text=f"Current password: ****", font=("Arial", 12))
            currentpassword.place(relx=0.33, rely=0.14)
            Label(changePasswordWindow, text=f"New password:", font=("Arial", 12)).place(relx=0.35, rely=0.24)
            passwordinput = Entry(changePasswordWindow, font=("Arial", 12))
            passwordinput.place(relx=0.25, rely=0.33)
            Button(changePasswordWindow, text="Change password", command=confirmChangePassword).place(relx=0.37, rely=0.43)

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

        menu1 = Notebook(settings)
        menu1.pack(anchor="center", fill="both", expand=True)

        securityframe = Frame(menu1, width=600, height=500)
        securityframe.pack(fill='both', expand=True)

        personalisationframe = Frame(menu1, width=600, height=500)
        personalisationframe.pack(fill='both', expand=True)

        systeminfoframe = Frame(menu1, width=600, height=500)
        systeminfoframe.pack(fill='both', expand=True)

        menu1.add(securityframe, text='Security')
        menu1.add(personalisationframe, text='Personalization')
        menu1.add(systeminfoframe, text="System info")

        # Security Icon

        iconsecurity = PhotoImage(file="UI/Menu/icons/security-icon.png")
        output_iconsecurity = Label(securityframe, image=iconsecurity)
        output_iconsecurity.image = iconsecurity
        output_iconsecurity.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(securityframe, text="Security", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        # Change password

        iconpassword = PhotoImage(file="UI/Login/icons/passwordicon.png")
        output_iconpassword = Label(securityframe, image=iconpassword)
        output_iconpassword.image = iconpassword
        output_iconpassword.place(relx=0.35, rely=0.15, anchor=CENTER)


        Label(securityframe, text=f"Current password: {output_password}", font=("Arial", 12)).place(relx=0.39, rely=0.14)        
        Button(securityframe, text="Change password", command=changePassword).place(relx=0.43, rely=0.21)

        # Change username

        iconusername = PhotoImage(file="UI/Menu/icons/usericon.png")
        output_iconusername = Label(securityframe, image=iconusername)
        output_iconusername.image = iconusername
        output_iconusername.place(relx=0.35, rely=0.29, anchor=CENTER)

        Label(securityframe, text=f"Current username: {output_username}", font=("Arial", 12)).place(relx=0.39, rely=0.28)
        Button(securityframe, text="Change username", command=changeUsername).place(relx=0.43, rely=0.34)

        # Personalization

        iconbackground = PhotoImage(file="UI/Menu/icons/background-icon.png")
        output_iconbackground = Label(personalisationframe, image=iconbackground)
        output_iconbackground.image = iconbackground
        output_iconbackground.place(relx=0.08, rely=0.09, anchor=CENTER)
        Label(personalisationframe, text="Personalization", font=("Arial", 20)).place(relx=0.14, rely=0.06)

        # System info

        iconsystem = PhotoImage(file="UI/Menu/icons/system-icon.png")
        output_iconsystem = Label(systeminfoframe, image=iconsystem)
        output_iconsystem.image = iconsystem
        output_iconsystem.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(systeminfoframe, text="System info", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        current_system = platform.system()

        username_file = open('System/Ressources/username.txt')
        current_username = username_file.read()
        username_file.close()

        current_processor = platform.processor()

        current_systemtype = platform.machine()

        Label(systeminfoframe, text=f"- System: {current_system}\n- Username: {current_username}\n- Processor: {current_processor}\n- System type: {current_systemtype}", font=("Arial", 12)).place(relx=0.15, rely=0.12)

        def changeColor(*args):
            fileColor = open("System/Ressources/background.txt", 'w')
            newColor = backgroundVar.get()
            if newColor == "Red":
                home.config(bg="red")
                fileColor.write("Red")
            elif newColor == "White":
                home.config(bg="white")
                fileColor.write("White")
            elif newColor == "Grey":
                home.config(bg="grey")
                fileColor.write("Grey")
            elif newColor == "Default":
                home.configure(background='SystemButtonFace')
                fileColor.write("Default")
            fileColor.close()

        fileColor = open("System/Ressources/background.txt", 'r')
        currentColor = fileColor.read()
        fileColor.close()

        backgroundVar = StringVar(personalisationframe)
        backgroundVar.set(f"Default") # default value

        colors = ("Red", "Default", "White", "Grey")

        Label(personalisationframe, text="Color:", font=("Arial", 20)).place(relx=0.46, rely=0.20)

        iconcolor = PhotoImage(file="UI/Menu/icons/color-icon.png")
        output_iconcolor = Label(personalisationframe, image=iconcolor)
        output_iconcolor.image = iconcolor
        output_iconcolor.place(relx=0.412, rely=0.24, anchor=CENTER)


        choiceColor = OptionMenu(personalisationframe, backgroundVar, colors[1], *colors, command=changeColor)
        choiceColor.place(relx=0.46, rely=0.28)

    def shutdownmaxpyos():
        home.withdraw()
        asking = mb.askquestion('MaxPyOS - Shutdown', 'Are you sure to shutdown ?')
        if asking == "yes":
            home.destroy()
            Shutdown.shutdown()
        elif asking == "no":
            home.deiconify()

    home = Tk()
    home.title("MaxPyOS - Home")
    home.geometry("720x450")
    home.resizable(False, False)
    home.iconbitmap("UI/Menu/icons/logo.ico")
    home.protocol("WM_DELETE_WINDOW", lambda: shutdownmaxpyos())

    fileColor = open("System/Ressources/background.txt", 'r')
    currentColor = fileColor.read()
    fileColor.close()

    if currentColor == "Default":
        home.configure(background='SystemButtonFace')
    elif currentColor == "Red":
        home.config(bg="red")
    elif currentColor == "Grey":
        home.config(bg="grey")
    elif currentColor == "White":
        home.config(bg="white")
    else:
        pass

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

        fileColor = open("System/Ressources/background.txt", 'r')
        currentColor = fileColor.read()
        fileColor.close()

        if currentColor == "Default":
            menu.configure(background='SystemButtonFace')
        elif currentColor == "Red":
            menu.config(bg="red")
        elif currentColor == "Grey":
            menu.config(bg="grey")
        elif currentColor == "White":
            menu.config(bg="white")
        else:
            pass

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

    iconfileexplorer = PhotoImage(file="UI/Menu/icons/fileexplorer-icon.png")
    output_iconfileexplorer = Button(home, text="FileExplorer",image=iconfileexplorer, command=fileexplorer)
    output_iconfileexplorer.image = iconfileexplorer
    output_iconfileexplorer.place(relx=0.25, rely=0.90, anchor=CENTER)

    iconmenucircled = PhotoImage(file="UI/Menu/icons/menucircled-icon.png")
    output_iconmenucircled = Button(home, text="Settings",image=iconmenucircled, command=MoreApps)
    output_iconmenucircled.image = iconmenucircled
    output_iconmenucircled.place(relx=0.50, rely=0.90, anchor=CENTER)