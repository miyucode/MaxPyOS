from System.Boot import Boot
from UI.Login import Login
from System.Restart.Restart import configure_start_command

from sys import platform

import os

def main():
	if platform == "win32":
		os.system("cls")

	Boot.Boot()
	Login.login()

if __name__ == '__main__':
	configure_start_command(main)
	main()
