from time import strftime
import sys
import time

def shutdown():
	sys.exit()
	print(f"[{strftime('%H:%M:%S')}]: Shutdown...")
	time.sleep(1)