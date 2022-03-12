from time import strftime
import sys
import time

def shutdown():
	print(f"[{strftime('%H:%M:%S')}]: Shutdown...")
	time.sleep(1)
	sys.exit()