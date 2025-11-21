import pygame
import random
import time

# Инициализация pygame
pygame.init()

# Размеры клетки и экрана
cell = 24
gw, gh = 22, 18
w, h = gw * cell, gh * cell
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake with Random Food")
clock = pygame.time.Clock()

# Шрифт для отображения счёта и уровня
font = pygame.font.SysFont(None, 28)

# Стены на экране
walls = set()
for x in range(gw):
    walls.add((x, 0))
    walls.add((x, gh - 1))
for y in range(gh):
    walls.add((0, y))
    walls.add((gw - 1, y))

# Функция для отрисовки клетки
def draw_cell(xy, col):
    x, y = xy
    pygame.draw.rect(screen, col, (x * cell, y * cell, cell, cell))

# Функция для случайного выбора пустой клетки для пищи
def empty_cell(snake):
    bad = set(snake) | walls
    free = [(x, y) for x in range(gw) for y in range(gh) if (x, y) not in bad]
    return random.choice(free)

# Класс для пищи с разными весами
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.randint(1, 3)  # Случайное значение пищи (1, 2 или 3)
        self.image = pygame.Surface((cell, cell))
        self.image.fill((255, 0, 0))  # Красный цвет для пищи
        self.rect = self.image.get_rect()
        self.rect.center = empty_cell([])  # Размещение пищи в случайной пустой клетке
        self.time_created = time.time()  # Время создания пищи

    def update(self):
        # Проверка на таймер — пища исчезает через 5 секунд
        if time.time() - self.time_created > 5:
            self.kill()  # Уничтожить пищу, если она старше 5 секунд

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]  # Начальная позиция змеи
        self.direction = (1, 0)  # Начальная направленность змеи (вправо)
        self.score = 0
        self.level = 1
        self.eaten = 0

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        # Увеличиваем змею
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body

    def change_direction(self, new_dir):
        # Проверка на противоположную направленность
        if (new_dir == (0, 1) and self.direction != (0, -1)) or \
           (new_dir == (0, -1) and self.direction != (0, 1)) or \
           (new_dir == (1, 0) and self.direction != (-1, 0)) or \
           (new_dir == (-1, 0) and self.direction != (1, 0)):
            self.direction = new_dir

    def get_head(self):
        return self.body[0]

# Инициализация змеи и пищи
snake = Snake()
food_group = pygame.sprite.Group()
food = Food()
food_group.add(food)

# Основной игровой цикл
running = True
while running:
    clock.tick(10 + (snake.level - 1) * 2)  # Увеличение скорости игры с каждым уровнем

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            if event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            if event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            if event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    snake.move()

    # Проверка на выход за границы экрана или столкновение с телом змеи
    head = snake.get_head()
    if head in walls or head in snake.body[1:]:
        running = False

    # Проверка на съедание пищи
    if head == food.rect.center:
        snake.grow()  # Змея растет
        snake.score += food.value  # Добавляем очки, равные весу пищи
        snake.eaten += 1
        if snake.eaten % 5 == 0:
            snake.level += 1  # Увеличение уровня каждые 5 съеденных пищи
        food_group.empty()  # Убираем старую пищу
        food = Food()  # Создаём новую пищу
        food_group.add(food)

    screen.fill((18, 18, 18))  # Задний фон

    # Отрисовка стен
    for wpos in walls:
        draw_cell(wpos, (60, 60, 60))

    # Отрисовка змеи
    for i, segment in enumerate(snake.body):
        draw_cell(segment, (0, 200, 0) if i == 0 else (0, 130, 0))

    # Отрисовка пищи
    food_group.update()  # Обновление состояния пищи (проверка на исчезновение)
    for f in food_group:
        draw_cell(f.rect.center, (200, 0, 0))  # Красный цвет для пищи

    # Отображение информации о счете и уровне
    hud = font.render(f"Score: {snake.score}  Level: {snake.level}", True, (255, 215, 0))
    screen.blit(hud, (10, 8))

    pygame.display.flip()

# Конец игры
pygame.quit()

