import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((10,5))
		self.image.fill((100,100,50))
		self.rect = self.image.get_rect()
		self.speed = 7

	def update(self):
		self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface((100,50))
		self.image.fill((100,180,60))
		self.rect = self.image.get_rect()
		self.width = width
		self.height = height
		self.speed = 5
		self.rect.center = [0, 50]
	def update(self):

		self.rect.x += self.speed
		if self.rect.x >= self.width-100:
			self.speed = -5
			self.rect.x -= 5
		if self.rect.x <= 0:
			self.speed = +5
			self.rect.x += 5