from time import strftime

start_command = None
def configure_start_command(command):
	global start_command
	start_command = command


def restart():
	print(f"[{strftime('%H:%M:%S')}]: Restarting...")
	start_command()
