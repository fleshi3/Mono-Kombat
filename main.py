import pygame
from pygame.locals import *
from Mono import MonoAlpha


# --- Main ---
def main():
	ma = MonoAlpha()
	ma.scream()
	
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

if __name__ == "__main__":
	main()
