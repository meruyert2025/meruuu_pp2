import pygame               # pygame кітапханасын қосу
import sys                  # жүйе функциялары үшін sys кітапханасын қосу
import random               # кездейсоқ сандарды генерациялау үшін random кітапханасын қосу
import time                 # уақытты басқару үшін time кітапханасын қосу
from pygame.locals import *  # Pygame локальды оқиғаларын қосу (QUIT, KEYDOWN, және т.б.)

# Инициализация pygame және аудио жүйелерін іске қосу
pygame.init()
pygame.mixer.init()  # pygame аудио жүйесін инициализациялау

# --- Константы ---
SCREEN_WIDTH = 400      # Экранның ені
SCREEN_HEIGHT = 600     # Экранның биіктігі
SPEED = 5              # Қаскөйлердің бастапқы жылдамдығы
SCORE = 0              # Бастапқы ұпай
COINS = 0              # Жиналған монеталар саны
FPS = 60               # Кадрлардың жиілігі (60 FPS)

# --- Түстер ---
BLUE = (0, 0, 255)      # Көк түс
RED = (255, 0, 0)       # Қызыл түс
GREEN = (0, 255, 0)     # Жасыл түс
BLACK = (0, 0, 0)       # Қара түс
WHITE = (255, 255, 255) # Ақ түс
YELLOW = (255, 255, 0)  # Сары түс

# --- Шрифт ---
font = pygame.font.SysFont("Verdana", 60)  # Үлкен шрифт (ойынның негізгі мәтіні үшін)
font_small = pygame.font.SysFont("Verdana", 20)  # Кіші шрифт (ұпай мен монеталар үшін)
game_over_text = font.render("Game Over", True, BLACK)  # "Game Over" мәтіні

# --- Экранды орнату ---
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Экран терезесін жасау
pygame.display.set_caption("Car Game")  # Терезенің атын орнату

# --- Аудио ---
pygame.mixer.music.load("/Users/meruert/Downloads/PygameTutorial_3_0/background.wav")  # Фондық музыканы жүктеу
pygame.mixer.music.play(-1)  # Музыкады зациклинг жасау
crash_sound = pygame.mixer.Sound("/Users/meruert/Downloads/PygameTutorial_3_0/crash.wav")  # Қақтығыс дыбысы

# --- Фон ---
background = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/AnimatedStreet.png")  # Фон суретін жүктеу

# --- Ойыншының сипаттамасы ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite базалық классын инициализациялау
        self.image = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/Player.png")  # Ойыншының суретін жүктеу
        self.rect = self.image.get_rect()  # Ойыншының тікбұрышын алу
        self.rect.center = (160, 520)  # Ойыншының бастапқы орналасуын орнату

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Басылған пернелерді алу
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  # Солға жылжыту, экранның сол жақ шекарасына жетпеу
            self.rect.move_ip(-5, 0)  # Жылжу влево
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:  # Оңға жылжыту, экранның оң жақ шекарасына жетпеу
            self.rect.move_ip(5, 0)  # Жылжу вправо

# --- Қаскөйлердің сипаттамасы ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite базалық классын инициализациялау
        self.image = pygame.image.load("/Users/meruert/Downloads/PygameTutorial_3_0/Enemy.png")  # Қаскөйлердің суретін жүктеу
        self.rect = self.image.get_rect()  # Қаскөйлердің тікбұрышын алу
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Қаскөйлерді кездейсоқ бастапқы орынға орнату

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Қаскөйлерді төменге жылжыту
        if self.rect.bottom > SCREEN_HEIGHT:  # Егер қаскөй экранның төменгі шекарасына жетсе
            SCORE += 1  # Ұпайды арттыру
            self.rect.top = 0  # Қаскөйді экранның жоғарғы жағына қайта орнату
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Қаскөйдің жаңа кездейсоқ орны

# --- Монеталардың сипаттамасы ---
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite базалық классын инициализациялау
        self.value = random.randint(1, 3)  # Монетаның кездейсоқ құнын таңдау (1, 2 немесе 3)
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)  # Монетаға арналған бет
        pygame.draw.circle(self.image, YELLOW, (12, 12), 12)  # Монетаны сары түспен салу
        self.rect = self.image.get_rect()  # Монетаның тікбұрышын алу
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-1500, -100))  # Монетаның кездейсоқ бастапқы орны

    def move(self):
        self.rect.move_ip(0, SPEED)  # Монетаны төменге жылжыту
        if self.rect.top > SCREEN_HEIGHT:  # Егер монета экраннан шықса
            self.rect.top = random.randint(-1500, -100)  # Монетаны экраннан жоғары орынға қайтару
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)  # Кездейсоқ жаңа орын

# --- Объектілерді жасау ---
P1 = Player()  # Ойыншы объектісін жасау
E1 = Enemy()   # Қаскөй объектісін жасау
C1 = Coin()    # Монета объектісін жасау

# --- Группалар ---
enemies = pygame.sprite.Group()  # Қаскөйлер тобы
enemies.add(E1)  # Қаскөйді тобына қосу

coins = pygame.sprite.Group()  # Монеталар тобы
coins.add(C1)  # Монетаны тобына қосу

all_sprites = pygame.sprite.Group()  # Барлық объектілер тобы
all_sprites.add(P1)  # Ойыншыны топқа қосу
all_sprites.add(E1)  # Қаскөйді топқа қосу
all_sprites.add(C1)  # Монетаны топқа қосу

# --- Оқиға: жылдамдықты арттыру ---
INC_SPEED = pygame.USEREVENT + 1  # Жылдамдықты арттыру оқиғасын жасау
pygame.time.set_timer(INC_SPEED, 1000)  # Әр 1000 миллисекунд сайын жылдамдықты арттыру

# --- Ойын циклі ---
FramePerSec = pygame.time.Clock()  # FPS бақылаушы

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # Жылдамдықты арттыру оқиғасы
            if SPEED < 15:  # Қаскөйлердің максималды жылдамдығы
                SPEED += 0.5  # Қаскөйлердің жылдамдығын арттыру
        if event.type == QUIT:  # Терезені жабу оқиғасы
            pygame.quit()  # Pygame-ды тоқтату
            sys.exit()  # Бағдарламаны тоқтату

    DISPLAYSURF.blit(background, (0, 0))  # Фонды экранға салу

    # Ойынның ұпайларын және монеталарды көрсету
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))  # Ұпайларды экранда көрсету
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))  # Монеталарды экранда көрсету

    for entity in all_sprites:  # Барлық объектілерді жылжыту
        entity.move()  # Әр объектіні жылжыту
        DISPLAYSURF.blit(entity.image, entity.rect)  # Әр объектіні экранға салу

    # Ойыншы мен қаскөйлердің соқтығысуын тексеру
    if pygame.sprite.spritecollideany(P1, enemies):  # Егер соқтығысса
        crash_sound.play()  # Қақтығыс дыбысын ойнату
        pygame.mixer.music.stop()  # Фондық музыканы тоқтату
        time.sleep(1)  # 1 секундтық кідіріс
        DISPLAYSURF.fill(RED)  # Экранды қызыл түспен толтыру
        DISPLAYSURF.blit(game_over_text, (30, 250))  # "Game Over" мәтінін көрсету
        final_text = font_small.render(f"Final Score: {SCORE}  Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_text, (60, 320))  # Соңғы ұпайлар мен монеталарды көрсету
        pygame.display.update()  # Экранды жаңарту
        time.sleep(3)  # 3 секундтық кідіріс
        pygame.quit()  # Pygame-ды тоқтату
        sys.exit()  # Бағдарламаны тоқтату

    # Ойыншы монеталарды жинауын тексеру
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)  # Монеталарды жинау
    for coin in collected_coins:
        COINS += coin.value  # Монетаның құнын қосу
        coin.rect.top = random.randint(-1500, -100)  # Монетаны экраннан жоғары жылжыту
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), coin.rect.top)  # Жаңа кездейсоқ орын

        if COINS >= 5:  # Егер 5 монета жиналса
            SPEED += 0.5  # Қаскөйлердің жылдамдығын арттыру
            COINS = 0  # Жиналған монеталарды нөлге теңестіру

    pygame.display.update()  # Экранды жаңарту
    FramePerSec.tick(FPS)  # FPS басқару
