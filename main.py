#!/bin/python
from display import *
from player import *
import time
import sys
import os
from kbhit import *
import events
import colorama
from v import *

Display.clear()
print('''
|----------------|
|THE BINDING OF  |
|   ISAAC:       |
|   ASCII EDITION|
|----------------|
''')#Welcome screen

time.sleep(0.3)
print(colorama.Fore.BLUE + "Press q to exit.\nMove with w/a/s/d.\nPress enter or space to start a new run." + colorama.Fore.RESET)

kb = KBHit()

while True:
	k_in = kb.getch()
	if k_in == "\n" or k_in == " ":
		break
	elif k_in == "q":
		events.keyAction("q")

V.runloop = True

Display.loadRoom("./resources/rooms/starting.room")#Loads the starting room
while V.runloop:
	time.sleep(0.03)
	Display.refresh()
	Display.drawPlayer()
	Player.printInfo()
	if kb.kbhit():
		k_in = kb.getch()
		events.keyAction(k_in)
	Player.checkDeath()

kb.set_normal_term()