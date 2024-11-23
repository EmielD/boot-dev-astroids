from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
	containers = ()

	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0

	def triangle(self):
			forward = pygame.Vector2(0, 1).rotate(self.rotation)
			right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
			a = self.position + forward * self.radius
			b = self.position - forward * self.radius - right
			c = self.position - forward * self.radius + right
			return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
		self.rotation = self.rotation % 360

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			print("Player pressing a")
			self.rotate(dt * -1)
		if keys[pygame.K_d]:
			print("Player pressing d")
			self.rotate(dt * 1)
		if keys[pygame.K_w]:
			print("Player pressing w")
			self.move(dt * 1)
		if keys[pygame.K_s]:
			print("Player pressing s")
			self.move(dt * -1)
		if keys[pygame.K_SPACE]:
			print("Player shoots")
			self.shoot()

		self.shoot_timer -= dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.shoot_timer >= 0:
			return 
		
		shot = Shot(self.position, SHOT_RADIUS)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
		shot.velocity *= PLAYER_SHOOT_SPEED
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
