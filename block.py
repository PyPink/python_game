import pygame
import random
class Block(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.image.fill((200,50,50))
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
		self.y = y
		self.x = x
		self.rect.x = random.randrange(self.x - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 8)



	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > self.y:
			self.rect.x = random.randrange(self.x - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)
