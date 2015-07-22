from v import *
import random
from player import *
import display
import time

def door():
	while True:
		dPos = random.choice("udlr") #u = up, d = down, l = left, r = right
		if dPos == "u" and V.SpawnPy != 7:
			V.replaceInRoom(7, 0, 'D')
			break

		elif dPos == "d" and V.SpawnPy != 7:
			V.replaceInRoom(7, 8, 'D')
			break
			
		elif dPos == "l" and V.SpawnPx != 1:
			V.replaceInRoom(0, 4, 'D')
			break

		elif dPos == "r" and V.SpawnPx != 13:
			V.replaceInRoom(14, 4, 'D')
			break

def room():
	display.Display.clear()
	print('''///////////////
///////////////
///////////////
///////////////
///////////////
///////////////
///////////////
///////////////
///////////////''')
	time.sleep(0.015)
	newRoom = random.choice("12")
	newRoom = "../rooms/" + newRoom + ".room"
	display.Display.loadRoom(newRoom)
