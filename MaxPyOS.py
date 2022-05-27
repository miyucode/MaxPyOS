from System.Boot import Boot
from System.Restart.Restart import configure_start_command

from UI.Login import Login

from sys import platform
from time import *

import os

def main():
	os.system('cls')

	Boot.Boot()

	username_file = open('System/Ressources/username.txt', 'r')
	username = username_file.read()

	password_file = open('System/Ressources/password.txt', 'r')
	password = password_file.read()

	password_file.close()
	username_file.close()

	print(f"[{strftime('%H:%M:%S')}]: Your username is \"{username}\" and your password is \"{password}\".")

	Login.login()

if __name__ == '__main__':
	configure_start_command(main)
	main()
