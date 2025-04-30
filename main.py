# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from shot import *
from asteroid import Asteroid
from asteroidfield import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updateables, drawables)
	Asteroid.containers = (asteroids, updateables, drawables)
	AsteroidField.containers = (updateables)
	Shot.containers = (shots, updateables, drawables)
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
	asteroidfield = AsteroidField()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updateables.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				sys.exit("Game over!")
		
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()
		
		screen.fill("black")
		
		for i in drawables:
			i.draw(screen)

		pygame.display.flip()
		result = clock.tick(60)
		dt = (result / 1000)


if __name__ == "__main__":
    main()
