from player import *
from v import *
import random

class Bomb:
	sprite = 'bq'
	bX = ""
	bY = ""
	delay = 33
	def deploy():
		if V.ThereIsBomb == False:
			Player.Bombs -= 1
			Bomb.bX = Player.pX
			Bomb.bY = Player.pY
			Bomb.delay = 0 
			V.ThereIsBomb = True

	def update():
		V.replaceInRoom(Bomb.bX, Bomb.bY, random.choice(Bomb.sprite))

		Bomb.delay += 1
		if Bomb.delay == 66:
			Bomb.explode()

	def explode():
		V.replaceInRoom(Bomb.bX, Bomb.bY, ' ')
		#DESTROY OBJECTS, DAMAGE PLAYER:
		print(colorama.Fore.RED, "BOOM!", colorama.Fore.RESET)

		if Player.pY == Bomb.bY and Player.pX  == Bomb.bX:
			Player.damaged(2)
		if V.room[Bomb.bY-1][Bomb.bX] == '&':
			V.replaceInRoom(Bomb.bX, Bomb.bY-1, ' ')
			
		elif V.room[Bomb.bY-1][Bomb.bX] == Player.sprite:
			Player.damaged(2)
			
		if V.room[Bomb.bY+1][Bomb.bX] == '&':
			V.replaceInRoom(Bomb.bX, Bomb.bY+1, ' ')
			
		elif V.room[Bomb.bY+1][Bomb.bX] == Player.sprite:
			Player.damaged(2)
		
		if V.room[Bomb.bY][Bomb.bX+1] == '&':
			V.replaceInRoom(Bomb.bX+1, Bomb.bY, ' ')
			
		elif V.room[Bomb.bY][Bomb.bX+1] == Player.sprite:
			Player.damaged(2)	
		
		if V.room[Bomb.bY][Bomb.bX-1] == '&':
			V.replaceInRoom(Bomb.bX-1, Bomb.bY, ' ')
			
		elif V.room[Bomb.bY][Bomb.bX-1] == Player.sprite:
			Player.damaged(2)
		
		if V.room[Bomb.bY-2][Bomb.bX] == '&':
			V.replaceInRoom(Bomb.bX, Bomb.bY-2, ' ')
			
		elif V.room[Bomb.bY-2][Bomb.bX] == Player.sprite:
			Player.damaged(2)
		
		try:
			if V.room[Bomb.bY+2][Bomb.bX] == '&':
				V.replaceInRoom(Bomb.bX, Bomb.bY+2, ' ')
			
			elif V.room[Bomb.bY+2][Bomb.bX] == Player.sprite:
				Player.damaged(2)
		
		except IndexError:
			pass
			
		if V.room[Bomb.bY][Bomb.bX-2] == '&':
			V.replaceInRoom(Bomb.bX-2, Bomb.bY, ' ')
			
		elif V.room[Bomb.bY][Bomb.bX-2] == Player.sprite:
			Player.damaged(2)
			
		try:
			if V.room[Bomb.bY][Bomb.bX+2] == '&':
				V.replaceInRoom(Bomb.bX+2, Bomb.bY, ' ')
				
			elif V.room[Bomb.bY][Bomb.bX+2] == Player.sprite:
				Player.damaged(2)
		except IndexError:
			pass
		
		if V.room[Bomb.bY+1][Bomb.bX+1] == '&':
			V.replaceInRoom(Bomb.bX+1, Bomb.bY+1, ' ')
			
		elif V.room[Bomb.bY+1][Bomb.bX+1] == Player.sprite:
			Player.damaged(2)
		
		if V.room[Bomb.bY-1][Bomb.bX-1] == '&':
			V.replaceInRoom(Bomb.bX-1, Bomb.bY-1, ' ')
			
		elif V.room[Bomb.bY-1][Bomb.bX-1] == Player.sprite:
			Player.damaged(2)
			
		if V.room[Bomb.bY+1][Bomb.bX-1] == '&':
			V.replaceInRoom(Bomb.bX-1, Bomb.bY+1, ' ')
		
		elif V.room[Bomb.bY+1][Bomb.bX-1] == Player.sprite:
			Player.damaged(2)
			
		if V.room[Bomb.bY-1][Bomb.bX+1] == '&':
			V.replaceInRoom(Bomb.bX+1, Bomb.bY-1, ' ')
			
		elif V.room[Bomb.bY-1][Bomb.bX+1] == Player.sprite:
			Player.damaged(2)
		
		time.sleep(0.05)
		Bomb.bY = ""
		Bomb.bX = ""
		V.ThereIsBomb = False
