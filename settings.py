class Settings():
	def __init__(self):
		# налаштування дисплея
		self.width = 1920
		self.height = 1080
		self.color = (255,255,255)
		self.FPS = 100

		self.running = True
		self.playing = True
		self.menu = False
		self.shop = True
		self.setting_screen = True

		# налаштування ігрока
		self.player_width = 30
		self.player_height = 30
		self.color_enemy = (0, 255, 0)
		self.player_x = self.width/2
		self.player_y = self.height/1.03
		self.speed = 6

		self.ACC = 1.3
		self.FRIC = -0.12
		# налаштування блока
		self.block_width = 40
		self.block_height = 40
		self.color_block = (100,100,100)
		self.speed_down = 7
		# налаштування обєктів
		self.hp = 10
		self.hp_buy = 10
		self.coin = 0
		self.price = 50
		self.score = 0

		self.color_black = (0,0,0)
		# налаштування кнопок
		self.left = False
		self.right = False

