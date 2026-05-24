x = random.randint(40, 550)
		y = random.randint(-400, 0)
		self.block = block.Block("sprite/blocks/pig_block.png", 0,0)

		enemy_width, enemy_height = self.block.rect.size
		ship_height = self.block.rect.height

		available_x = self.settings.width - (2 * enemy_width)
		available_y = self.settings.height - (18* enemy_height) - ship_height

		number_block_x = available_x // (2 * enemy_width)
		number_block_y = available_y // (2 * enemy_height)

		number_rows = available_y // (2 * enemy_height)
		
		for row_number in range(number_rows):
			for block_number in range(number_block_x):
				x = random.randint(40, 550)
				y = random.randint(-400, 0)

				self.block = block.Block("sprite/blocks/pig_block.png", x,y)

				self.block.x = enemy_width + 2 * enemy_width * block_number
				
				self.block.rect.x = self.block.x
				self.block.rect.y = self.block.rect.height + 4 * self.block.rect.height * row_number

				self.block_sprite.add(self.block)
				self.all_sprite.add(self.block)

		if self.settings.playing == False:
			self.all_sprite.remove(block)