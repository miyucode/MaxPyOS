from System.Boot import Boot
from System.Restart.Restart import configure_start_command

from UI.Login import Login

from UI.Menu.menu import Home

from time import *

import sys
import os

try:
	if sys.argv[1] == "admin":
		admin_file1 = open('System/Ressources/admin.txt', 'w')
		admin_file1.write("yes")
		admin_file1.close()
except:
	pass

def main():
	os.system('cls')

	Boot.Boot()

	username_file = open('System/Ressources/username.txt', 'r')
	username = username_file.read()

	password_file = open('System/Ressources/password.txt', 'r')
	password = password_file.read()

	admin_file = open('System/Ressources/admin.txt', 'r')
	admin_mode = admin_file.read()

	admin_file.close()
	password_file.close()
	username_file.close()

	if admin_mode == "yes":
		admin_file2 = open('System/Ressources/admin.txt', 'w')
		admin_file2.write("no")
		admin_file2.close()
		Home()
	else:
		print(f"[{strftime('%H:%M:%S')}]: Your username is \"{username}\" and your password is \"{password}\".")
		Login.login()

if __name__ == '__main__':
	configure_start_command(main)
	main()
