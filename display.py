from v import *
from player import *
import rand
class Display:
	def loadRoom(filename):
		with open(filename) as f:#Load room and save it to a string list
			V.room = [line.rstrip('\n') for line in open(filename)]
		Player.pX = 7
		Player.pY = 4
		rand.door() #Selects random place for door

	def refresh():
		Display.clear()
		for i in range(0,len(V.room)): #Prints room
			print(V.room[i])

	def drawPlayer():
			templist = list(V.room[Player.pY])
			templist[Player.pX] = Player.sprite
			V.room[Player.pY] = ''.join(templist)
	def clear():
		print("\x1B[2J\x1B[H") #Clear console