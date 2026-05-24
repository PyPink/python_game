import pygame
import time
import sys
import random
import json

import settings
import player
import spawn_items
import button

from enemy import Enemy
from enemy import Bullet
from block import Block

class Main():
	def __init__(self):
		# імпорт файлів
		pygame.init()
		self.settings = settings.Settings()
		self.enemy = Enemy(self.settings.width, self.settings.height)
		self.button_arrow = button.Arrow()
		
		self.menu = self.settings.menu
		self.shop = self.settings.shop
		self.setting_screen = self.settings.setting_screen

		self.filename = 'saver_coin.json'
		
		# гравітація
		self.vec = pygame.math.Vector2

		# створення дисплея
		self.screen = pygame.display.set_mode((self.settings.width, self.settings.height), pygame.FULLSCREEN)
		
		self.frames = pygame.time.Clock()

		self.left = self.settings.left
		self.right = self.settings.right

		self.hp = self.settings.hp
		self.hp_buy = self.settings.hp_buy
		self.price = self.settings.price
	
		self.coin = self.settings.coin
		self.score = self.settings.score
		self.enemy_spawn_time = 2000
		self.last_spawn_time = pygame.time.get_ticks()
		# текст
		self.myfont = pygame.font.Font("grand9k_pixel/Grand9k Pixel.ttf", 30)
		self.font = pygame.font.Font("grand9k_pixel/Grand9k Pixel.ttf", 50)

		# налаштування спрайтів
		self.create_sprite()
		self.sprite()

		# групи спрайтів
		self.group_sprite()

	def game_loop(self):
		# ігровий цикл
		self.create_block()
		
		while not self.settings.playing:
			self.screen.fill(self.settings.color)
			self.move()

			self.draw_sprite()
			self.sprite_settings()

			self.other_settings()
			self.text_generate()
			self.hit()
			self.update()
			
	def move(self):
		# налаштування кнопок клавіатури
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()
			
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_ESCAPE:
					self.block_sprite.remove(self.block)
					self.menu = False
					self.settings.playing = True
					
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = event.pos

				for click in self.arrow_sprite:
					
					if click.rect.collidepoint(position):
						pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
						
						for block in self.block_sprite.copy():
							self.block_sprite.remove(block)
							self.all_sprite.remove(block)
							self.score = 0
							self.hp = self.hp_buy
							self.menu = False
							self.settings.playing = True
		
		if self.left == True:
			self.sprite_sheet_player.rect.x -= self.settings.speed
		
		if self.right == True:
			self.sprite_sheet_player.rect.x += self.settings.speed

	def other_settings(self):

		self.score += 1

		# час за який спавниться ворог
		self.current_time = pygame.time.get_ticks()
		
		if self.current_time-self.last_spawn_time >= self.enemy_spawn_time:
			
			self.all_sprite.add(self.enemy)
			self.enemy_sprite.add(self.enemy)
			self.last_spawn_time = self.current_time

		for i in self.enemy_sprite.copy():
			
			if i.rect.x >= self.settings.width:
				
				self.all_sprite.remove(self.enemy)
				self.enemy_sprite.remove(self.enemy)
				print(1)	

		if self.hp <= 0:

			pygame.mixer.Sound('sound/mixkit-arcade-space-shooter-dead-notification-272.wav').play()
			
			self.all_sprite.remove(self.block.rect)
			self.all_sprite.remove(self.block.rect)
			

			for block in self.block_sprite.copy():
				self.block_sprite.remove(block)
				self.all_sprite.remove(block)

				self.sprite_sheet.rect.x = random.randint(10, 550)
				self.sprite_sheet.rect.y = random.randint(-3100, -2000)

				self.sprite_sheet_coin.rect.x = random.randint(10, 550)
				self.sprite_sheet_coin.rect.y = random.randint(-3100, -2000)

				self.sprite_sheet_player.rect.x = self.settings.width/2
				self.sprite_sheet_player.rect.y = self.settings.height/1.1

				self.score = 0
				self.hp = self.hp_buy

				self.settings.playing = True
				self.menu = False
			
			self.text = self.font.render("You lose", 20, (200,0,0))
			self.screen.blit(self.text, (self.settings.width/2.8, self.settings.height/2.5))

	
	def create_sprite(self):

		# Анімація серце
		self.sprite_sheet_image = pygame.image.load("sprite/health/health4.png").convert_alpha()

		self.sprite_sheet = spawn_items.Health(self.sprite_sheet_image)

		self.animation_list = []
		self.animation_steps = [3]
		self.action = 0 
		self.last_update = pygame.time.get_ticks()

		self.animation_cooldown = 100
		self.frame = 0 
		self.step_counter = 0
		

		self.black = self.settings.color_black

		# анімація монети
		self.sprite_sheet_image_coin = pygame.image.load("sprite/coin/coin4.png").convert_alpha()
		self.sprite_sheet_coin = spawn_items.Coin(self.sprite_sheet_image_coin)

		self.animation_list_coin = []
		self.animation_steps_coin = [12]
		self.action_coin = 0 
		self.last_update_coin = pygame.time.get_ticks()

		self.animation_cooldown_coin = 100
		self.frame_coin = 0 
		self.step_counter_coin = 0

		# анімація персонажа
		self.sprite_sheet_image_player = pygame.image.load("sprite/player_sprites/player4.png").convert_alpha()
		self.sprite_sheet_player = player.Player(self.sprite_sheet_image_player, self.settings.width/2, self.settings.height/1.1)

		self.animation_list_player = []
		self.animation_steps_player = [1]
		self.action_player = 0 
		self.last_update_player = pygame.time.get_ticks()

		self.animation_cooldown_player = 100
		self.frame_player = 0 
		self.step_counter_player = 0

	def sprite(self):

		# анімація серця
		for animation in self.animation_steps:
			self.temp_img_list = []
			
			for _ in range(animation):
				self.temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, 25,25,3, self.black))
				self.step_counter += 1
			
			self.animation_list.append(self.temp_img_list)

		# анімація монети
		for animation in self.animation_steps_coin:
			self.temp_img_list_coin = []
			
			for _ in range(animation):
				self.temp_img_list_coin.append(self.sprite_sheet_coin.get_image(self.step_counter_coin, 25,25,3, self.black))
				self.step_counter_coin += 1
			
			self.animation_list_coin.append(self.temp_img_list_coin)

		# анімація персонажа
		for animation in self.animation_steps_player:
			self.temp_img_list_player = []
			
			for _ in range(animation):
				self.temp_img_list_player.append(self.sprite_sheet_player.get_image(self.step_counter_player, 25,25,2, (0,0,0), self.settings.width/2, self.settings.height/1.1))
				self.step_counter_player += 1
			
			self.animation_list_player.append(self.temp_img_list_player)

	def sprite_settings(self):
		# налаштування анімації серця {{
		self.current_time = pygame.time.get_ticks()

		if self.current_time - self.last_update >= self.animation_cooldown:
			self.frame += 1
			self.last_update = self.current_time
			
			if self.frame >= len(self.animation_list[self.action]):
				self.frame = 0
				
		self.screen.blit(self.animation_list[self.action][self.frame], (20,0))

		# }}

		# налаштування анімації монети {{
		self.current_time_coin = pygame.time.get_ticks()

		if self.current_time_coin - self.last_update_coin >= self.animation_cooldown_coin:
			self.frame_coin += 1
			self.last_update_coin = self.current_time_coin
			
			if self.frame_coin >= len(self.animation_list_coin[self.action_coin]):
				self.frame_coin = 0

		self.screen.blit(self.animation_list_coin[self.action_coin][self.frame_coin], (20,60))

		# }}

		# налаштування анімації персонажа {{
		self.current_time_player = pygame.time.get_ticks()

		if self.current_time_player - self.last_update_player >= self.animation_cooldown_player:
			self.frame_player += 1
			self.last_update_player = self.current_time_player
			
			if self.frame_player >= len(self.animation_list_player[self.action_player]):
				self.frame_player = 0

		# }}		

	def draw_sprite(self):

		# створення обєктів на екрані
		self.health_sprite.add(self.sprite_sheet)

		for entity in self.all_sprite:
			self.screen.blit(entity.image, entity.rect)
		for entity in self.block_sprite:
			self.screen.blit(entity.image, entity.rect)
		for entity in self.player_sprite:
			self.screen.blit(self.animation_list_player[self.action_player][self.frame_player], entity.rect)

		self.screen.blit(self.animation_list[self.action][self.frame], (self.sprite_sheet.rect.x, self.sprite_sheet.rect.y))

		self.screen.blit(self.animation_list_coin[self.action_coin][self.frame_coin], (self.sprite_sheet_coin.rect.x, self.sprite_sheet_coin.rect.y))

	def group_sprite(self):

		# групи спрайтів
		self.all_sprite = pygame.sprite.Group()

		self.all_sprite.add(self.button_arrow)

		self.enemy_sprite = pygame.sprite.Group()
		
		self.bullet_sprite = pygame.sprite.Group()

		self.player_sprite = pygame.sprite.Group()
		self.player_sprite.add(self.sprite_sheet_player)
		

		self.block_sprite = pygame.sprite.Group()

		self.health_sprite = pygame.sprite.Group()
		self.health_sprite.add(self.sprite_sheet)

		self.coin_sprite = pygame.sprite.Group()
		self.coin_sprite.add(self.sprite_sheet_coin)

		self.arrow_sprite = pygame.sprite.Group()
		self.arrow_sprite.add(self.button_arrow)

	def hit(self):

		# зіткнення спрайтів
		for block in self.player_sprite:
			sprite_hit = pygame.sprite.spritecollide(block,self.block_sprite ,True)

			for hit in sprite_hit:
				self.hp -= 5
				pygame.mixer.Sound('sound/mixkit-small-hit-in-a-game-2072.wav').play()

								
		# зіткнення із серцем
		for health in self.player_sprite:
			sprite_hit = pygame.sprite.spritecollide(health, self.health_sprite, False)
			
			for hit in sprite_hit:
				self.hp += 1
				self.sprite_sheet.rect.x = random.randint(10, 550)
				self.sprite_sheet.rect.y = random.randint(-3100, -2000)
				pygame.mixer.Sound('sound/mixkit-video-game-health-recharge-2837.wav').play()

				if self.hp >= self.hp_buy:
					self.hp = self.hp_buy
				if self.hp <= 0:
					self.hp = 0

		# зіткнення із монетою
		for coin in self.coin_sprite:
			sprite_hit = pygame.sprite.spritecollide(coin, self.player_sprite, False)
			
			for hit in sprite_hit:
				self.coin += random.randint(1,100)
				pygame.mixer.Sound('sound/mixkit-winning-a-coin-video-game-2069.wav').play()
				self.sprite_sheet_coin.rect.x = random.randint(40, 550)
				self.sprite_sheet_coin.rect.y = random.randint(-1100, -900)

	def create_block(self):

		# створення блоків
		x = random.randint(10,30)
		
		for i in range(x):
			self.block = Block(self.settings.width, self.settings.height)

			self.block_sprite.add(self.block)
			self.all_sprite.add(self.block)

	def text_generate(self):

		# генерація тексту
		self.hptext = self.myfont.render(f" {self.hp}/{self.hp_buy}", 20, (0,0,0))
		self.screen.blit(self.hptext, (80, 10))

		self.cointext = self.myfont.render(" {0}".format(self.coin), 20, (0,0,0))
		self.screen.blit(self.cointext, (80, 70))

		self.scoretext = self.myfont.render("score: {0}".format(self.score), 20, (0,0,0))
		self.screen.blit(self.scoretext, (40, 120))
		
	def update(self):

		# оновлення і FPS

		self.enemy_sprite.update()
		self.bullet_sprite.update()

		self.arrow_sprite.update(self.settings.width/1.04, self.settings.height*0.04)
		self.health_sprite.update(self.settings.height, self.settings.width*0, self.settings.width)
		self.coin_sprite.update(self.settings.height, self.settings.width*0, self.settings.width)

		self.sprite_sheet_player.update(self.settings.speed, self.settings.width/1, self.settings.ACC, self.settings.FRIC)
		self.block_sprite.update()

		pygame.display.update()
		self.frames.tick(self.settings.FPS)

	def main_menu(self):

		# головне меню
		self.play = button.Play(self.settings.width/2, self.settings.height/7, self.settings.width/4, self.settings.height/6)
		self.shop = button.Shop(self.settings.width/2, self.settings.height/3, self.settings.width/4, self.settings.height/6)
		self.setting_button = button.Settings_Button("sprite/button/settings.png",self.settings.width/2, self.settings.height/1.8, self.settings.width/4, self.settings.height/6)
		self.exit = button.Exit(self.settings.width/2, self.settings.height/1.3, self.settings.width/4, self.settings.height/6)

		# self.screen_main = pygame.display.set_mode((self.settings.width, self.settings.height)) 
		self.frame_menu = pygame.time.Clock()
		self.FPS_MENU = 60
		self.c = 0
		self.all_button_sprite = pygame.sprite.Group()

		self.all_button_sprite.add(self.play)
		self.all_button_sprite.add(self.shop)
		self.all_button_sprite.add(self.setting_button)
		self.all_button_sprite.add(self.exit)

		self.sprite_play = pygame.sprite.Group()
		self.sprite_play.add(self.play)

		self.sprite_shop = pygame.sprite.Group()
		self.sprite_shop.add(self.shop)

		self.setting_sprite = pygame.sprite.Group()
		self.setting_sprite.add(self.setting_button)

		self.sprite_exit = pygame.sprite.Group()
		self.sprite_exit.add(self.exit)

		while not self.menu:
			
			# цикл меню
			self.screen.fill((50,100,100))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					position = event.pos
					for click in self.sprite_play:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							for block in self.block_sprite.copy():
								self.block_sprite.remove(block)
								self.score = 0
								self.hp = self.hp_buy
							self.menu = True
							self.settings.playing = False

					for click in self.sprite_shop:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							for block in self.block_sprite.copy():
								self.block_sprite.remove(block)
								self.score = 0
								self.hp = self.hp_buy
							self.menu = True
							self.shop = False

					for click in self.setting_sprite:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							for block in self.block_sprite.copy():
								self.block_sprite.remove(block)
								self.score = 0
								self.hp = self.hp_buy
							self.menu = True
							self.setting_screen = False

					for click in self.sprite_exit:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							self.settings.running = False
							self.menu = True
							self.settings.playing = True

			for entity in self.all_button_sprite:
				self.screen.blit(entity.image, entity.rect)

			pygame.display.update()
			self.frame_menu.tick(self.FPS_MENU)

	def shop_menu(self):

		# меню магазину
		self.screen_shop = pygame.display.set_mode((self.settings.width, self.settings.height)) 
		self.frame_shop = pygame.time.Clock()
		self.FPS_shop = 60

		self.myfont_shop = pygame.font.Font("grand9k_pixel/Grand9k Pixel.ttf", 30)
		self.font_shop = pygame.font.Font("grand9k_pixel/Grand9k Pixel.ttf", 50)


		self.button_arrow = button.Arrow()
		self.background_shop = button.Back_Shop("sprite/background/back_shop.png", self.settings.width/2, self.settings.height/2, self.settings.width/1.2, self.settings.height/1.2)
		
		self.buttons_shop_sprite = pygame.sprite.Group()

		self.buttons_shop_sprite.add(self.button_arrow)
		self.buttons_shop_sprite.add(self.background_shop)
		
		self.button_arrow_sprite = pygame.sprite.Group()
		self.button_arrow_sprite.add(self.button_arrow)

		self.sprite_shop_player_1 = pygame.sprite.Group()
		self.sprite_shop_player_1.add(self.sprite_shop)

		# Кнопка купівлі
		self.buy_button = button.Button()
		self.buy_button_sprite = pygame.sprite.Group()
		self.buy_button_sprite.add(self.buy_button)
		self.buttons_shop_sprite.add(self.buy_button)
	
		while not self.shop:
			
			
			self.screen_shop.fill((50,100,100))
			
			self.hptext_shop = self.myfont_shop.render(f" {self.hp_buy} hp max.", 20, (0,0,0))
			self.cointext_shop = self.myfont_shop.render(f" {self.coin} coin", 30, (0,0,0))
			self.pricetext_shop = self.myfont_shop.render(f" {self.price} coin", 25, (0,0,0))
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					position = event.pos 
					for click in self.button_arrow_sprite:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							self.shop = True
							self.menu = False
							self.settings.playing = True

					for click in self.sprite_shop_player_1:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()

					if self.coin >= self.price:
						for click in self.buy_button_sprite:
							if click.rect.collidepoint(position):
								pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
								
								self.hp += 1
								self.coin -= self.price
								self.price *= 2

			for entity in self.buttons_shop_sprite:
				self.screen_shop.blit(entity.image, entity.rect)
			self.screen_shop.blit(self.hptext_shop, (210, 125))
			self.screen_shop.blit(self.cointext_shop, (100, 20))
			self.screen_shop.blit(self.pricetext_shop, (180,180))

			self.button_arrow.update(30, 30)
			pygame.display.update()
			self.frame_shop.tick(self.FPS_shop)

	def setting_screen_game(self):

		# налаштування гри
		self.screen_setting = pygame.display.set_mode((self.settings.width, self.settings.height))
		self.button_arrow_s = button.Arrow()

		self.buttons_setting_sprite = pygame.sprite.Group()
		self.buttons_setting_sprite.add(self.button_arrow_s)

		while not self.setting_screen:
			self.screen.fill((50,100,100))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					position = event.pos 
					for click in self.button_arrow_sprite:
						if click.rect.collidepoint(position):
							pygame.mixer.Sound('sound/SWRYQ7A-tap-click.mp3').play()
							self.setting_screen = True
							self.menu = False
							self.settings.playing = True

			for entity in self.buttons_setting_sprite:
				self.screen_setting.blit(entity.image, entity.rect)
			
			self.button_arrow_s.update(30, 30)
			pygame.display.update()
			self.frame_shop.tick(self.FPS_shop)

if __name__ == '__main__':
	# головний цикл
	m = Main()

	while m.settings.running:
		m.main_menu()
		m.shop_menu()
		m.setting_screen_game()
		m.game_loop()