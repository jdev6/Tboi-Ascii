import colorama
import time
import sys
import kbhit

class V:
	room = 0
	runloop = False
	info = 0
	ThereIsBomb = False
	ThereAreTears = False
	tear1 = 0
	
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
	
def pauseG():
		#PRESS ENTER OR SPACE. Q TO EXIT
		kb = kbhit.KBHit()
		while True:
			k_in = kb.getch()
			if k_in == "\n" or k_in == " ":
				break
			elif k_in == "q":
				exitG()