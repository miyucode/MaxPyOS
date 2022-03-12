from time import strftime
import os
import time

def restart():
	print(f"[{strftime('%H:%M:%S')}]: Restart...")
	time.sleep(0.75)
	path = "MaxPyOS.py"
	os.system(f"{path}")
	print(f"[{strftime('%H:%M:%S')}]: Restart effectued with success.")
	print(f"[{strftime('%H:%M:%S')}]: Welcome back on MaxPyOS !")