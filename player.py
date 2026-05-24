import pygame
vec = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
	def __init__(self, image,width, height):
		super().__init__()
		self.sheet = image
		self.rect = self.sheet.get_rect()
		

		self.pos = vec((width, height))
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def get_image(self, frame, width, height, scale,colour, x, y):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)
		self.rect = image.get_rect()
		
		self.rect.center = [x, y]

		return image

	def update(self, speed, width, ACC, FRIC):
		self.acc = vec(0,0)
		pressed_key = pygame.key.get_pressed()

		if pressed_key[pygame.K_LEFT]:
			self.acc.x = -ACC
		if pressed_key[pygame.K_RIGHT]:
			self.acc.x = ACC

		self.acc.x += self.vel.x * FRIC
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		self.rect.midbottom = self.pos

		if self.pos.x <= 30:
			self.pos.x = 30
		if self.pos.x >= width-30:
			self.pos.x = width-30
