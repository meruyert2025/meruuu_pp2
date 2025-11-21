import pygame
import sys
import random
import time
from pygame.locals import *

# Инициализация pygame и звуков
pygame.init()
pygame.mixer.init()

# --- Константы ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # начальная скорость врагов
SCORE = 0  # начальный счёт
COINS = 0  # количество собранных монет
FPS = 60  # частота кадров

# --- Цвета ---
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# --- Шрифт ---
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# --- Окно ---
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# --- Звук ---
pygame.mixer.music.load("/Users/meruert/Downloads/PygameTutorial_3_0/background.wav")
pygame.mixer.music.play(-1)  # зацикливаем музыку
crash_sound = pygame.mixer.Sound("/Users/meruert/Downloads/PygameTutorial_3_0/crash.wav")

# --- Фон ---
background = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/AnimatedStreet.png")

# --- Игрок ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)  # движение влево
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)  # движение вправо

# --- Враг ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # движение врага
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1  # увеличиваем счёт, когда враг выходит за экран
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# --- Монеты с разными весами ---
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.randint(1, 3)  # случайная ценность монеты (1, 2 или 3)
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (12, 12), 12)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-1500, -100))
    
    def move(self):
        self.rect.move_ip(0, SPEED)  # движение монеты
        if self.rect.top > SCREEN_HEIGHT:  # если монета выходит за экран
            self.rect.top = random.randint(-1500, -100)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

# --- Создание объектов ---
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# --- Событие увеличения скорости ---
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # увеличиваем скорость каждую секунду

# --- Игровой цикл ---
FramePerSec = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if SPEED < 15:  # Максимальная скорость врагов
                SPEED += 0.5  # Увеличиваем скорость врагов каждую секунду
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Проверка на столкновение с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.mixer.music.stop()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        final_text = font_small.render(f"Final Score: {SCORE}  Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_text, (60, 320))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # Проверка на сбор монет
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        COINS += coin.value  # Добавляем стоимость монеты
        coin.rect.top = random.randint(-1500, -100)  # Перемещаем монету за пределы экрана
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), coin.rect.top)

        if COINS >= 5:  # Когда собрали 5 монет
            SPEED += 0.5  # Увеличиваем скорость врагов
            COINS = 0  # Сбрасываем количество собранных монет

    pygame.display.update()
    FramePerSec.tick(FPS)

