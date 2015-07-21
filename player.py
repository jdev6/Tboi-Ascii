from v import *
import rand
import colorama
import time
class Player:
	pX = 0
	pY = 0
	Health = 6
	MaxHealth = 6
	CompletedRooms = 0
	sprite = '@' #The sprite for the player. This can be changed
	def move(direction):

		if direction == "w": #Move upwards
			if V.room[Player.pY-1][Player.pX] == ' ':
				Player.pY = Player.pY - 1 #Change sprite coordinates
				#Erase the player's sprite in previous coordinates:
				templist = list(V.room[Player.pY+1])
				templist[Player.pX] = ' '
				V.room[Player.pY+1] = ''.join(templist)
			#Check if there is a door
			elif V.room[Player.pY-1][Player.pX] == 'D':
				Player.CompletedRooms += 1
				rand.room()
			#Check if there are spikes
			elif V.room[Player.pY-1][Player.pX] == 'w':
				Player.damaged(1)

		if direction == "s": #Move downwards
			if V.room[Player.pY+1][Player.pX] == ' ':
				Player.pY = Player.pY + 1 #Change sprite coordinates
				#Erase the player's sprite in previous coordinates
				templist = list(V.room[Player.pY-1])
				templist[Player.pX] = ' '
				V.room[Player.pY-1] = ''.join(templist)
			#Check if there is a door
			elif V.room[Player.pY+1][Player.pX] == 'D':
				Player.CompletedRooms += 1
				rand.room()
			#Check if there are spikes
			elif V.room[Player.pY+1][Player.pX] == 'w':
				Player.damaged(1)

		if direction == "a": #Move to the left
			if V.room[Player.pY][Player.pX-1] == ' ':
				Player.pX = Player.pX - 1 #Change sprite coordinates
				#Erase the player's sprite in previous coordinates
				templist = list(V.room[Player.pY])
				templist[Player.pX+1] = ' '
				V.room[Player.pY] = ''.join(templist)
			#Check if there is a door
			elif V.room[Player.pY][Player.pX-1] == 'D':
				Player.CompletedRooms += 1
				rand.room()
			#Check if there are spikes
			elif V.room[Player.pY][Player.pX-1] == 'w':
				Player.damaged(1)

		if direction == "d": #Move to the right
			if V.room[Player.pY][Player.pX+1] == ' ':
				Player.pX = Player.pX + 1 #Change sprite coordinates
				#Erase the player's sprite in previous coordinates
				templist = list(V.room[Player.pY])
				templist[Player.pX-1] = ' '
				V.room[Player.pY] = ''.join(templist)
				#Check if there is a door
			elif V.room[Player.pY][Player.pX+1] == 'D':
				Player.CompletedRooms += 1
				rand.room()
			#Check if there are spikes
			elif V.room[Player.pY][Player.pX+1] == 'w':
				Player.damaged(1)
	
	def checkDeath():
		if Player.Health <= 0:
			print(colorama.Fore.RED, '''
				|---------|
				|GAME OVER|
				|---------|
				''', colorama.Fore.RESET)
			print("\nYou have died, it's game over.")
			V.runloop = False

	def printInfo():
		print(colorama.Fore.GREEN, "\n Health = ", Player.Health, "/", Player.MaxHealth, "  -->  ", format(((Player.Health / Player.MaxHealth) * 100), '.2f'), "%/100 %", colorama.Fore.RESET)
		print(colorama.Fore.YELLOW, "Rooms completed = ", Player.CompletedRooms, colorama.Fore.RESET)

	def damaged(p):
		Player.Health -= 1
		print(colorama.Fore.RED, "OUCH!", colorama.Fore.RESET)
		time.sleep(0.1)