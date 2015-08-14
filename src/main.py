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
from bomb import *

colorama.init()
Display.clear()
print('''
|----------------|
|THE BINDING OF  |
|   ISAAC:       |
|   ASCII EDITION|
|----------------|
''')#Welcome screen

time.sleep(0.15)
Display.loadInfo()
time.sleep(0.15)
print(colorama.Fore.BLUE + "Press q to exit.\nMove with w/a/s/d.\nFire tears with i/j/k/l.\nPress p to pause game.\nPress enter or space to start a new run." + colorama.Fore.RESET)

kb = KBHit()

pauseG()

V.runloop = True

Display.loadRoom("./rooms/starting.room")#Loads the starting room
while V.runloop:
	time.sleep(0.03)
	Display.refresh()
	Display.drawPlayer()
	Player.printInfo()

	if kb.kbhit():
		k_in = kb.getch()
		events.keyAction(k_in)
	
	if V.ThereAreTears == True:
		Tear.update()

	if V.ThereIsBomb == True:
		Bomb.update()

	Player.checkDeath()

kb.set_normal_term()
