from v import *
import random
from player import *
import display
import time

def door():
	dPos = random.choice("udlr") #u = up, d = down, l = left, r = right
	if dPos == "u":
		templist = list(V.room[0])
		templist[7] = 'D'
		V.room[0] = ''.join(templist)
	if dPos == "d":
		templist = list(V.room[8])
		templist[7] = 'D'
		V.room[8] = ''.join(templist)
	if dPos == "l":
		templist = list(V.room[7])
		templist[0] = 'D'
		V.room[4] = ''.join(templist)
	if dPos == "r":
		templist = list(V.room[7])
		templist[14] = 'D'
		V.room[4] = ''.join(templist)

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
	newRoom = "./resources/rooms/" + newRoom + ".room"
	display.Display.loadRoom(newRoom)