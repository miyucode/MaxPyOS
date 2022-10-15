from System.Shutdown import Shutdown
from System.Restart import Restart
from System.Utilities import RaiseError
from System.Shell import Shell

from UI.Login import Login

from Apps.Notepad.app import notepad
from Apps.WeatherApp.app import weatherapp
from Apps.FileExplorer.app import fileexplorer
from Apps.MusicPlayer.app import musicplayer
from Apps.CalendarApp.app import calendarapp
from Apps.MaxWeb.app import maxweb

from tkinter import *
from tkinter.ttk import *

from platform import *

from time import strftime

from datetime import datetime

import tkinter.messagebox as mb

import requests

import platform
import psutil


import datetime

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

        def openCalendarAppViaMoreApps():
            moreapps.destroy()
            calendarapp()

        def openMaxWebViaMoreApps():
            moreapps.destroy()
            maxweb()

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
        Label(moreapps, text="Weather", font=("Arial", 10)).place(relx=0.56, rely=0.22)

        iconcalendarapp = PhotoImage(file="UI/Menu/icons/calendar-icon.png")
        output_iconcalendarapp = Button(moreapps, text="Calendar", image=iconcalendarapp, command=openCalendarAppViaMoreApps)
        output_iconcalendarapp.image = iconcalendarapp
        output_iconcalendarapp.place(relx=0.75, rely=0.15, anchor=CENTER)
        Label(moreapps, text="Calendar", font=("Arial", 10)).place(relx=0.70, rely=0.22)

        iconmaxweb = PhotoImage(file="UI/Menu/icons/maxweb-icon.png")
        output_iconmaxweb = Button(moreapps, text="MaxWeb", image=iconmaxweb, command=openMaxWebViaMoreApps)
        output_iconmaxweb.image = iconmaxweb
        output_iconmaxweb.place(relx=0.15, rely=0.35, anchor=CENTER)
        Label(moreapps, text="MaxWeb", font=("Arial", 10)).place(relx=0.10, rely=0.42)

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

        wifiinfoframe = Frame(menu1, width=600, height=500)
        wifiinfoframe.pack(fill='both', expand=True)

        menu1.add(securityframe, text='Security')
        menu1.add(personalisationframe, text='Personalization')
        menu1.add(systeminfoframe, text="System info")
        menu1.add(wifiinfoframe, text="Internet")

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
        output_iconbackground.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(personalisationframe, text="Personalization", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        # System info

        iconsystem = PhotoImage(file="UI/Menu/icons/system-icon.png")
        output_iconsystem = Label(systeminfoframe, image=iconsystem)
        output_iconsystem.image = iconsystem
        output_iconsystem.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(systeminfoframe, text="System Info", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        current_system = platform.platform()

        username_file = open('System/Ressources/username.txt')
        current_username = username_file.read()
        username_file.close()

        current_processor = platform.processor()

        current_systemtype = platform.machine()

        Label(systeminfoframe, text=f"- System: {current_system}\n- Username: {current_username}\n- Processor: {current_processor}\n- System type: {current_systemtype}", font=("Arial", 12)).place(relx=0.15, rely=0.12)

        iconprocessor = PhotoImage(file="UI/Menu/icons/processor-icon.png")
        output_iconprocessor = Label(systeminfoframe, image=iconprocessor)
        output_iconprocessor.image = iconprocessor
        output_iconprocessor.place(relx=0.05, rely=0.32, anchor=CENTER)
        Label(systeminfoframe, text="Processor Info", font=("Arial", 20)).place(relx=0.10, rely=0.29)

        cpufreq = psutil.cpu_freq()

        Label(systeminfoframe, text=f"- Physical cores: {psutil.cpu_count(logical=False)}\n- Total Cores: {psutil.cpu_count(logical=True)}\n- Frequency: Not available\n- Max Frequency: Not available\n- Min Frequency: {cpufreq.min:.2f}Mhz", font=("Arial", 12)).place(relx=0.15, rely=0.37)

        def update_cpuusage():
            current_cpuusage = psutil.cpu_percent()
            cpuusage.config(text=f"- Total CPU Usage: {current_cpuusage}%")
            cpuusage.after(1000, update_cpuusage)

        cpuusage = Label(systeminfoframe, text=f"- Total CPU Usage: {psutil.cpu_percent()}%", font=("Arial", 12))
        cpuusage.place(relx=0.15, rely=0.53)
        update_cpuusage()

        iconcredits = PhotoImage(file="UI/Menu/icons/human_head-icon.png")
        output_iconcredits = Label(systeminfoframe, image=iconcredits)
        output_iconcredits.image = iconcredits
        output_iconcredits.place(relx=0.05, rely=0.65, anchor=CENTER)
        Label(systeminfoframe, text="Credits", font=("Arial", 20)).place(relx=0.10, rely=0.62)

        Label(systeminfoframe, text="- Creator: Miyu (https://github.com/miyucode)", font=("Arial", 12)).place(relx=0.15, rely=0.69)
        Label(systeminfoframe, text="- MaxPyOS Creation Date: 15 April 2022", font=("Arial", 12)).place(relx=0.15, rely=0.74)
        Label(systeminfoframe, text="- Current version: MaxPyOS-1.2 (https://github.com/miyucode/MaxPyOS)", font=("Arial", 12)).place(relx=0.15, rely=0.79)

        # Wi-Fi Info & All

        iconwifi = PhotoImage(file="UI/Menu/icons/wifi-icon.png")
        output_iconwifi = Label(wifiinfoframe, image=iconwifi)
        output_iconwifi.image = iconwifi
        output_iconwifi.place(relx=0.05, rely=0.05, anchor=CENTER)
        Label(wifiinfoframe, text="Wi-Fi", font=("Arial", 20)).place(relx=0.10, rely=0.02)

        timeout = 1
        try:
            requests.head("http://www.google.com/", timeout=timeout)
            iconwifiactive = PhotoImage(file="UI/Menu/icons/wifi-yes.png")
            output_wifiactive = Label(wifiinfoframe, image=iconwifiactive)
            output_wifiactive.image = iconwifiactive
            output_wifiactive.place(relx=0.05, rely=0.25, anchor=CENTER)
            wifi_state = Label(wifiinfoframe, text="The internet connection is active.", font=("Arial", 12))
            wifi_state.place(relx=0.10, rely=0.24)
        except requests.ConnectionError:
            iconwifinotactive = PhotoImage(file="UI/Menu/icons/wifi-no.png")
            output_wifinotactive = Label(wifiinfoframe, image=iconwifinotactive)
            output_wifinotactive.image = iconwifinotactive
            output_wifinotactive.place(relx=0.05, rely=0.25, anchor=CENTER)
            wifi_state = Label(wifiinfoframe, text="The internet connection is down.", font=("Arial", 12))
            wifi_state.place(relx=0.10, rely=0.24)

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
            elif newColor == "Blue":
                home.config(bg="blue")
                fileColor.write("Blue")
            elif newColor == "Aqua":
                home.configure(background='SystemButtonFace')
                fileColor.write("Aqua")                
            elif newColor == "Default":
                home.configure(background='SystemButtonFace')
                fileColor.write("Default")
            fileColor.close()

        fileColor = open("System/Ressources/background.txt", 'r')
        currentColor = fileColor.read()
        fileColor.close()

        backgroundVar = StringVar(personalisationframe)
        backgroundVar.set(f"Choose one color") # default value

        colors = ("Red", "Choose one color", "Default", "White", "Grey", "Blue", "Aqua")

        Label(personalisationframe, text="Color:", font=("Arial", 20)).place(relx=0.46, rely=0.17)

        iconcolor = PhotoImage(file="UI/Menu/icons/color-icon.png")
        output_iconcolor = Label(personalisationframe, image=iconcolor)
        output_iconcolor.image = iconcolor
        output_iconcolor.place(relx=0.412, rely=0.21, anchor=CENTER)


        choiceColor = OptionMenu(personalisationframe, backgroundVar, colors[1], *colors, command=changeColor)
        choiceColor.place(relx=0.44, rely=0.24)

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
    elif currentColor == "Blue":
        home.config(bg="blue")
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
        elif currentColor == "Blue":
            menu.config(bg="blue")
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

    current_day = datetime.date.today().day
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year

    def time():
        actual_time=strftime('%H:%M')
        current_time.config(text=actual_time)
        current_time.after(1000, time)
        
    current_time = Label(home, text=f"", font=("Monospace", 10))
    current_time.place(relx=0.92, rely=0.92)
    time()

    Label(home, text=f"{current_day}/{current_month}/{current_year}", font=("Monospace", 10)).place(relx=0.90, rely=0.87)

    home.mainloop()