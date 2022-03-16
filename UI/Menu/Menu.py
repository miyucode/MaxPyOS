from System.Shutdown import Shutdown
from System.Restart import Restart
from UI.Login import Login

from Apps.Notepad.app import notepad

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from time import strftime

import tkinter.messagebox as mb
import tkinter as tk

def Home():
    def MoreApps():
        l = 0

    def Notepad():
        notepad()

    def Settings():

        password = open('System/Ressources/password.txt', 'r')
        output_password = password.read()
        password.close()

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

        menu1.add(securityframe, text='Security')
        menu1.add(personalisationframe, text='Personalization')

        # Change password

        iconpassword = PhotoImage(file="UI/Login/icons/passwordicon.png")
        output_iconpassword = Label(securityframe, image=iconpassword)
        output_iconpassword.image = iconpassword
        output_iconpassword.place(relx=0.35, rely=0.15, anchor=CENTER)

        iconsecurity = PhotoImage(file="UI/Menu/icons/security-icon.png")
        output_iconsecurity = Label(securityframe, image=iconsecurity)
        output_iconsecurity.image = iconsecurity
        output_iconsecurity.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(securityframe, text="Security", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        Label(securityframe, text=f"Current password: {output_password}", font=("Arial", 12)).place(relx=0.39, rely=0.14)        
        Button(securityframe, text="Change password", command=changePassword).place(relx=0.43, rely=0.21)

        # Personalization

        iconbackground = PhotoImage(file="UI/Menu/icons/background-icon.png")
        output_iconbackground = Label(personalisationframe, image=iconbackground)
        output_iconbackground.image = iconbackground
        output_iconbackground.place(relx=0.08, rely=0.08, anchor=CENTER)
        Label(personalisationframe, text="Personalization", font=("Arial", 20)).place(relx=0.14, rely=0.06)

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
        backgroundVar.set(f"{currentColor}") # default value

        colors = ("Default", "Red", "White", "Grey")

        Label(personalisationframe, text="Color:", font=("Arial", 15)).place(relx=0.45, rely=0.20)

        choiceColor = OptionMenu(personalisationframe, backgroundVar, colors[1], *colors, command=changeColor)
        choiceColor.place(relx=0.45, rely=0.27)

    home = Tk()
    home.title("MaxPyOS - Home")
    home.geometry("720x450")
    home.resizable(False, False)
    home.iconbitmap("UI/Menu/icons/logo.ico")

    fileColor = open("System/Ressources/background.txt", 'r')
    currentColor = fileColor.read()
    fileColor.close()

    if currentColor == "Default":
        home.config(bg="")
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
            menu.config(bg="")
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

    test = tk.Frame(home, bg="red")
    test.pack()

    iconlogotaskbar = PhotoImage(file="UI/Menu/icons/logo-png.png")
    output_iconlogotaskbar = Button(home, image=iconlogotaskbar, command=menu)
    output_iconlogotaskbar.image = iconlogotaskbar
    output_iconlogotaskbar.place(relx=0.05, rely=0.90, anchor=CENTER)

    iconoptions = PhotoImage(file="UI/Menu/icons/options-icon.png")
    output_iconoptions = Button(home, text="Settings",image=iconoptions, command=Settings)
    output_iconoptions.image = iconoptions
    output_iconoptions.place(relx=0.15, rely=0.90, anchor=CENTER)

    iconnotepad = PhotoImage(file="UI/Menu/icons/notepad-icon.png")
    output_iconnotepad = Button(home, text="Settings",image=iconnotepad, command=Notepad)
    output_iconnotepad.image = iconnotepad
    output_iconnotepad.place(relx=0.25, rely=0.90, anchor=CENTER)

    iconmenucircled = PhotoImage(file="UI/Menu/icons/menucircled-icon.png")
    output_iconmenucircled = Button(home, text="Settings",image=iconmenucircled, command=MoreApps)
    output_iconmenucircled.image = iconmenucircled
    output_iconmenucircled.place(relx=0.50, rely=0.90, anchor=CENTER)