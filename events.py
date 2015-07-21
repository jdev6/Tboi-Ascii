import sys
import time
from player import *
import colorama
from display import *

def keyAction(key):
	if key == "q":
		Display.clear()
		print(colorama.Fore.RED, "OK. Exiting game...\n", colorama.Fore.RESET)
		time.sleep(0.3)
		print("Done")
		sys.exit()
	elif key == "w" or key == "a" or key == "s" or key == "d":
		Player.move(key)
