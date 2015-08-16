import time
import pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load("./sound/Songloop.mp3")
pygame.mixer.music.play()
currentt = lambda: int(round(time.time() * 1000))
x = currentt()
running = True
final = 162148
while running:
  time.sleep(0.1)
  print(currentt()-x)
  if currentt()-x >= final:
    final *= 2
    x = currentt()
    print("Kek")
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    time.sleep(1)