import pygame

class Arrow(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("sprite/button/arrow2.png")
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect = self.image.get_rect()
	def update(self, x, y):
		self.x = x 
		self.y = y
		self.rect.center = [self.x, self.y]

class Play(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load("sprite/button/play.png")	
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

class Shop(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load("sprite/button/shop.png")
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load("sprite/button/exit.png")
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]


class Back_Shop(pygame.sprite.Sprite):
	def __init__(self, image, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

class Down_Shop(pygame.sprite.Sprite):
	def __init__(self, image, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

class Skins_Shop(pygame.sprite.Sprite):
	def __init__(self, image, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

class Settings_Button(pygame.sprite.Sprite):
	def __init__(self, image, x, y, width, height):
		super().__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (width,height))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]


class Button(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((30,30))
		self.image.fill((60,60,60))
		self.rect = self.image.get_rect()
		self.rect.center = [200,150]