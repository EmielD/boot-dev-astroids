import sys
import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

	print("Starting astroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updateable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroids_group = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()

	AsteroidField.containers = (updateable_group,)
	Player.containers = (updateable_group, drawable_group)
	Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
	Shot.containers = (shots_group, updateable_group, drawable_group)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		for updateable in updateable_group:
			updateable.update(dt)

		for asteroid in asteroids_group:
			for shot in shots_group:
				if asteroid.collision_with(shot):
					print("bang!")
					asteroid.split()
					shot.kill()


		for asteroid in asteroids_group:
			if asteroid.collision_with(player):
				print("GAME OVER!")
				sys.exit()

		for drawable in drawable_group:
			drawable.draw(screen)

		pygame.display.flip()

		dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
	main()
