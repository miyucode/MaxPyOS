from System.Boot import Boot
from UI.Login import Login

from sys import platform

import os

def main():
	if platform == "win32":
		os.system("cls")

	Boot.Boot()
	Login.login()

if __name__ == '__main__':
	main()