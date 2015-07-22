import sys
import time
from display import *
from player import *
from bomb import *
import colorama
from v import *

def keyAction(key):
	if key == "q":
		exitG()

	elif key == "w" or key == "a" or key == "s" or key == "d":
		Player.move(key)

	elif key == "e":
		if Player.Bombs > 0:
			Bomb.deploy()
	elif key == "p":
		Display.clear()
		print("Press enter or space to resume game...")
		Display.pause()
