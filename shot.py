import pygame
from circleshape import CircleShape


class Shot(CircleShape):
	containers = ()

	def __init__(self, position, radius):
		super().__init__(position.x, position.y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
