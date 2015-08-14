from v import *
import rand
import colorama
import time
import uuid

class Tear():
	sprite = '.'
	tX = 0
	tY = 0
	tdir = ''
	tmp = 0
		
	def update():
		Tear.tmp += 1
		if Tear.tmp == Player.tspeed:
			Tear.tmp = 0
			if V.tear1.tdir == 'i':
				if V.room[V.tear1.tX][V.tear1.tY-1] != '&' and V.room[V.tear1.tX][V.tear1.tY-1] != '#':
					V.tear1.tY -= 1
					V.replaceInRoom(V.tear1.tX, V.tear1.tY+1, ' ')

		V.replaceInRoom(V.tear1.tX, V.tear1.tY, Tear.sprite)
		
class Player:
	tspeed = 9
	pX = 0
	pY = 0
	Health = 6
	MaxHealth = 6
	CompletedRooms = 0
	Bombs = 99
	SpawnPx = 7
	SpawnPy = 4
	Coins = 0
	sprite = '@' #The sprite for the player. This can be changed

	def move(direction):
		try:
			if direction == "w": #Move upwards
				if V.room[Player.pY-1][Player.pX] == ' ':
					Player.pY -= 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates:
					V.replaceInRoom(Player.pX, Player.pY+1, ' ')
				#Check if there is a door
				elif V.room[Player.pY-1][Player.pX] == 'D':
					Player.CompletedRooms += 1
					Player.SpawnPx = 7
					Player.SpawnPy = 7
					rand.room()
				#Check if there are spikes
				elif V.room[Player.pY-1][Player.pX] == 'w':
					Player.damaged(1)
				#Check if there are coins
				elif V.room[Player.pY-1][Player.pX] == 'c':
					Player.pY -= 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates:
					V.replaceInRoom(Player.pX, Player.pY+1, ' ')
					Player.Coins += 1				
	
			if direction == "s": #Move downwards
				if V.room[Player.pY+1][Player.pX] == ' ':
					Player.pY += 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX, Player.pY-1, ' ')
				#Check if there is a door
				elif V.room[Player.pY+1][Player.pX] == 'D':
					Player.CompletedRooms += 1
					Player.SpawnPx = 7
					Player.SpawnPy = 1
					rand.room()
				#Check if there are spikes
				elif V.room[Player.pY+1][Player.pX] == 'w':
					Player.damaged(1)
				#Check if there is a coin
				elif V.room[Player.pY+1][Player.pX] == 'c':
					Player.pY += 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX, Player.pY-1, ' ')
					Player.Coins += 1				
	
			if direction == "a": #Move to the left
				if V.room[Player.pY][Player.pX-1] == ' ':
					Player.pX -= 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX+1, Player.pY, ' ')
				#Check if there is a door
				elif V.room[Player.pY][Player.pX-1] == 'D':
					Player.CompletedRooms += 1
					Player.SpawnPx = 13
					Player.SpawnPy = 4
					rand.room()
				#Check if there are spikes
				elif V.room[Player.pY][Player.pX-1] == 'w':
					Player.damaged(1)
				#Check if there is a coin
				elif V.room[Player.pY][Player.pX-1] == 'c':
					Player.pX -= 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX+1, Player.pY, ' ')
					Player.Coins += 1
	
			if direction == "d": #Move to the right
				if V.room[Player.pY][Player.pX+1] == ' ':
					Player.pX += 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX-1, Player.pY, ' ')
					#Check if there is a door
				elif V.room[Player.pY][Player.pX+1] == 'D':
					Player.CompletedRooms += 1
					Player.SpawnPx = 1
					Player.SpawnPy = 4
					rand.room()
				#Check if there are spikes
				elif V.room[Player.pY][Player.pX+1] == 'w':
					Player.damaged(1)
				#Check if there is a coin
				elif V.room[Player.pY][Player.pX+1] == 'c':
					Player.pX += 1 #Change sprite coordinates
					#Erase the player's sprite in previous coordinates
					V.replaceInRoom(Player.pX-1, Player.pY, ' ')
					Player.Coins += 1
		except IndexError:
				pass
	
	def checkDeath():
		if Player.Health <= 0:
			print(colorama.Fore.RED, '''
				|---------|
				|GAME OVER|
				|---------|
				''', colorama.Fore.RESET)
			print("Press enter or space to exit game...")
			pauseG()
			V.runloop = False

	def printInfo():
		print(colorama.Fore.GREEN, "\n Health = ", Player.Health, "/", Player.MaxHealth, "  -->  ", format(((Player.Health / Player.MaxHealth) * 100), '.2f'), "%/100 %", colorama.Fore.RESET)
		print(colorama.Fore.CYAN, "Completed rooms = ", Player.CompletedRooms, colorama.Fore.RESET)
		print(colorama.Fore.MAGENTA, "Bombs = ", Player.Bombs, colorama.Fore.RESET)
		print(colorama.Fore.YELLOW, "Coins = ", Player.Coins, colorama.Fore.RESET)

	def damaged(p):
		Player.Health -= p
		print(colorama.Fore.RED, "OUCH!", colorama.Fore.RESET)
		time.sleep(0.05)

	def fireTear(direction):
			V.tear1 = Tear()
			V.tear1.tX = Player.pX
			V.tear1.tY = Player.pY
			V.tear1.tdir = direction