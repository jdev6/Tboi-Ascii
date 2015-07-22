import colorama
import time
import sys

class V:
	room = 0
	runloop = False
	info = 0
	ThereIsBomb = False
	SpawnPx = ""
	SpawnpY = ""
	
	def replaceInRoom(x, y, ic):
		templist = list(V.room[y])
		templist[x] = ic
		V.room[y] = ''.join(templist)

def exitG():
	print("\x1B[2J\x1B[H") #Clear console
	print(colorama.Fore.RED, "OK. Exiting game...\n", colorama.Fore.RESET)
	time.sleep(0.3)
	print("Done")
	sys.exit()
