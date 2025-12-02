import pygame               # pygame кітапханасын қосу
import random               # Кездейсоқ сандарды генерациялау үшін random кітапханасын қосу
import time                 # Уақытты басқару үшін time кітапханасын қосу

# Инициализация pygame
pygame.init()  # Pygame-ды инициализациялау

# Экранның өлшемдері
cell = 24                   # Әр ұяшықтың өлшемі (24x24 пиксель)
gw, gh = 22, 18             # Ойын алаңының ені мен биіктігі (22x18 ұяшық)
w, h = gw * cell, gh * cell # Экранның толық өлшемі
screen = pygame.display.set_mode((w, h))  # Экран терезесін жасау
pygame.display.set_caption("Snake with Random Food")  # Экранның атын орнату
clock = pygame.time.Clock()  # FPS-ты бақылау үшін сағат

# Шрифтты орнату (ұпайлар мен деңгей көрсету үшін)
font = pygame.font.SysFont(None, 28)

# Экрандағы қабырғалар (тұрақты кедергілер)
walls = set()  # Қабырғалар жинағы
for x in range(gw):  # Экранның жоғарғы және төменгі қабырғаларын жасау
    walls.add((x, 0))  # Жоғарғы қабырға
    walls.add((x, gh - 1))  # Төменгі қабырға
for y in range(gh):  # Экранның сол жақ және оң жақ қабырғаларын жасау
    walls.add((0, y))  # Сол жақ қабырға
    walls.add((gw - 1, y))  # Оң жақ қабырға

# Функция ұяшықты салу
def draw_cell(xy, col):
    x, y = xy
    pygame.draw.rect(screen, col, (x * cell, y * cell, cell, cell))  # Ұяшықты салу

# Функция кездейсоқ бос ұяшық таңдау
def empty_cell(snake):
    bad = set(snake) | walls  # Бос емес ұяшықтар (змеи мен қабырғалар)
    free = [(x, y) for x in range(gw) for y in range(gh) if (x, y) not in bad]  # Бос ұяшықтарды табу
    return random.choice(free)  # Кездейсоқ бос ұяшықты таңдау

# Қызықты монеталар класы
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Sprite класына мұрагерлік
        self.value = random.randint(1, 3)  # Монетаның кездейсоқ мәні (1, 2 немесе 3)
        self.image = pygame.Surface((cell, cell))  # Монетаны салу үшін бет жасау
        self.image.fill((255, 0, 0))  # Монетаның түсі (қызыл)
        self.rect = self.image.get_rect()  # Монетаның тікбұрышы
        self.rect.center = empty_cell([])  # Монетаны кездейсоқ бос ұяшыққа орналастыру
        self.time_created = time.time()  # Пищаның жасалған уақыты

    def update(self):
        # Егер монета 5 секундтан ұзақ уақыт болса, оны жою
        if time.time() - self.time_created > 5:
            self.kill()  # Монетаны жою

# Змеи класы
class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]  # Змеи бастапқы денесі
        self.direction = (1, 0)  # Змеи бастапқы бағыты (оңға)
        self.score = 0  # Бастапқы ұпай
        self.level = 1  # Бастапқы деңгей
        self.eaten = 0  # Жиналған азық саны

    def move(self):
        head = self.body[0]  # Змеи басы
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])  # Жаңа бас позициясы
        self.body = [new_head] + self.body[:-1]  # Змеи денесін жылжыту

    def grow(self):
        # Змеи өсуін қамтамасыз ету
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body  # Змеи денесіне жаңа бөлік қосу

    def change_direction(self, new_dir):
        # Қарсы бағытта қозғалмауды тексеру
        if (new_dir == (0, 1) and self.direction != (0, -1)) or \
           (new_dir == (0, -1) and self.direction != (0, 1)) or \
           (new_dir == (1, 0) and self.direction != (-1, 0)) or \
           (new_dir == (-1, 0) and self.direction != (1, 0)):
            self.direction = new_dir  # Бағытты өзгерту

    def get_head(self):
        return self.body[0]  # Змеи басын алу

# Инициализация змеи и пищи
snake = Snake()  # Змеи объектісін жасау
food_group = pygame.sprite.Group()  # Пища тобы
food = Food()  # Пища объектісін жасау
food_group.add(food)  # Пищаны топқа қосу

# --- Негізгі ойын циклі ---
running = True
while running:
    clock.tick(10 + (snake.level - 1) * 2)  # Ойынның жылдамдығы деңгейіне байланысты артады

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Ойынды жабу
            running = False
        if event.type == pygame.KEYDOWN:  # Перне басу
            if event.key == pygame.K_ESCAPE:  # ESC пернесі арқылы ойынды тоқтату
                running = False
            if event.key == pygame.K_UP:  # Жоғарыға бағыттау
                snake.change_direction((0, -1))
            if event.key == pygame.K_DOWN:  # Төменге бағыттау
                snake.change_direction((0, 1))
            if event.key == pygame.K_LEFT:  # Солға бағыттау
                snake.change_direction((-1, 0))
            if event.key == pygame.K_RIGHT:  # Оңға бағыттау
                snake.change_direction((1, 0))

    snake.move()  # Змеи жылжыту

    # Экран шекарасына немесе змеи денесіне соқтығысуды тексеру
    head = snake.get_head()
    if head in walls or head in snake.body[1:]:  # Егер змеи қабырғаға немесе денесіне соқтығысса
        running = False

    # Пищаны жеп, ұпайларды есептеу
    if head == food.rect.center:
        snake.grow()  # Змеи өсуі
        snake.score += food.value  # Пищаның құнына сәйкес ұпай қосу
        snake.eaten += 1
        if snake.eaten % 5 == 0:  # Әр 5 тамақтан кейін деңгей арттыру
            snake.level += 1
        food_group.empty()  # Ескі тағамды өшіру
        food = Food()  # Жаңа тағамды жасау
        food_group.add(food)  # Жаңа тағамды топқа қосу

    screen.fill((18, 18, 18))  # Экранның фонын қою түспен толтыру

    # Қабырғаларды салу
    for wpos in walls:
        draw_cell(wpos, (60, 60, 60))  # Қабырғаларды салу

    # Змеи денесін салу
    for i, segment in enumerate(snake.body):
        draw_cell(segment, (0, 200, 0) if i == 0 else (0, 130, 0))  # Бас бөлік жасыл, қалғандары қара-жасыл

    # Пищаны салу
    food_group.update()  # Пищаның күйін жаңарту
    for f in food_group:
        draw_cell(f.rect.center, (200, 0, 0))  # Қызыл түспен тағамды салу

    # Ұпайлар мен деңгей туралы ақпаратты көрсету
    hud = font.render(f"Score: {snake.score}  Level: {snake.level}", True, (255, 215, 0))
    screen.blit(hud, (10, 8))  # Экранға ұпай мен деңгейді шығару

    pygame.display.flip()  # Экранды жаңарту

# Ойын аяқталды
pygame.quit()  # Pygame-ды тоқтату
