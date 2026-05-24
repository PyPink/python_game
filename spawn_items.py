import pygame
import random

class Coin(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.sheet = image
		self.rect = self.sheet.get_rect()
		self.rect.center = [random.randrange(1,2520), random.randrange(-1000,-1)]

	def get_image(self, frame, width, height, scale,colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)
		self.rect = image.get_rect()
		self.rect.center = [random.randrange(1,2520), random.randrange(-1000,-1)]


		return image

	def update(self, height, w_1, w_2):
		
		self.rect.y += 4
		x = random.randint(w_1, w_2)
		y = random.randint(-1100, -900)
		if self.rect.y >= height:
			self.rect.x = x
			self.rect.y = y

class Health(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.sheet = image
		self.rect = self.sheet.get_rect()
		

	def get_image(self, frame, width, height, scale,colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)
		self.rect = image.get_rect()

		return image

	def update(self, height, w_1, w_2):
		self.rect.y += 4
		x = random.randint(w_1, w_2)
		y = random.randint(-3100, -2000)
		if self.rect.y >= height:
			self.rect.x = x
			self.rect.y = y