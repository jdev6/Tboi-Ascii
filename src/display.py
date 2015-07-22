from v import *
from player import *
import rand
from bomb import *
import kbhit
import colorama

class Display:
	def pause():
		#PRESS ENTER OR SPACE. Q TO EXIT
		kb = kbhit.KBHit()
		while True:
			k_in = kb.getch()
			if k_in == "\n" or k_in == " ":
				break
			elif k_in == "q":
				exitG()

	def loadInfo():
		with open("../vinfo") as f:#Load room and save it to a string list
			V.info = [line.rstrip('\n') for line in open("../vinfo")]
		for j in range(0, len(V.info)):
			print(V.info[j])

	def loadRoom(filename):
		with open(filename) as f:#Load room and save it to a string list
			V.room = [line.rstrip('\n') for line in open(filename)]
		Player.pX = Player.SpawnPx
		Player.pY = Player.SpawnPy
		V.SpawnPx = Player.SpawnPx
		V.SpawnPy = Player.SpawnPx
		rand.door() #Selects random place for door

	def refresh():
		Display.clear()
		for i in range(0,len(V.room)): #Prints room
			print(V.room[i])

	def drawPlayer():
			V.replaceInRoom(Player.pX, Player.pY, Player.sprite)
			
	def clear():
		print("\x1B[2J\x1B[H") #Clear console
