import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Колір
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Розмір вікна
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Гра з NPC та пулями")

# Клас для представлення гравця
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

    def update(self):
        # Оновлюємо позицію гравця за допомогою координат миші
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, -1)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Клас для представлення пулі
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.direction = direction

    def update(self):
        self.rect.y += 5 * self.direction
        if self.rect.bottom < 0 or self.rect.top > height:
            self.kill()

# Клас для представлення NPC
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(50, 150)
        self.direction = random.choice([-1, 1])
        self.speed = 2

    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.left <= 0 or self.rect.right >= width:
            self.direction *= -1
            self.rect.y += 20

        # Ємулюємо випуск пуль NPC
        if random.randint(1, 100) < 3:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 1)
        all_sprites.add(bullet)
        bullets.add(bullet)


# Групи спрайтів
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
npcs = pygame.sprite.Group()

# Гравець
player = Player()
all_sprites.add(player)

# Створення NPC


# Основний цикл гри
running = True
clock = pygame.time.Clock()

while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()

    # Оновлення
    all_sprites.update()

    # Перевірка зіткнень пуль NPC з гравцем
    hits = pygame.sprite.spritecollide(player, bullets, False)
    if hits:
        running = False

    # Перевірка зіткнень пуль гравця з NPC
    hits = pygame.sprite.groupcollide(npcs, bullets, True, True)
    for hit in hits:
        # Тут ви можете виконати додаткові дії, наприклад, зарахувати очки гравцю

        # Створення нового NPC
        npc = NPC()
        all_sprites.add(npc)
        npcs.add(npc)

    # Відображення
    window.fill((0, 0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

    # FPS
    clock.tick(60)

# Завершення Pygame
pygame.quit()
