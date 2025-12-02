# task 2
import pygame
import random

# Pygame-ды инициализациялау
pygame.init()

# Экранның өлшемдері
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Ball Game")
clock = pygame.time.Clock()

# Ойыншының доп параметрлері
player_radius = 15  # Ойыншының доп радиусы
player_x = WIDTH // 2  # Бастапқы X позициясы
player_y = HEIGHT - 50  # Бастапқы Y позициясы
player_speed = 5  # Ойыншының жылдамдығы

# Қаскөйлердің параметрлері
enemy_width = 60  # Қаскөйлердің ені
enemy_height = 20  # Қаскөйлердің биіктігі
enemy_speed = 3  # Қаскөйлердің жылдамдығы

# Түстерді анықтау
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Ойыншының допты салу
def draw_player(x, y):
    pygame.draw.circle(screen, BLUE, (x, y), player_radius)

# Қаскөйлерді салу
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_width, enemy_height))

# Қаскөйлердің қозғалысын тексеру
def move_enemy(enemy_x, enemy_y):
    enemy_x -= enemy_speed
    if enemy_x < 0:
        enemy_x = WIDTH  # Қаскөй экранның оң жағынан шығып кетсе, сол жағынан қайта пайда болады
    return enemy_x

# Ойынның негізгі циклі
def main():
    global player_x, player_y  # Ойыншының позициясы

    enemy_x = random.randint(WIDTH, WIDTH + 200)  # Қаскөйдің бастапқы X орны
    enemy_y = random.randint(50, HEIGHT - 150)  # Қаскөйдің бастапқы Y орны
    game_over = False  # Ойын аяқталды ма?
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Терезе жабылғанда
                game_over = True

        # Пернелерді басу арқылы қозғалыс
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_radius > 0:  # Солға жылжыту
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_radius < WIDTH:  # Оңға жылжыту
            player_x += player_speed
        if keys[pygame.K_UP] and player_y - player_radius > 0:  # Жоғарыға жылжыту
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + player_radius < HEIGHT:  # Төменге жылжыту
            player_y += player_speed

        # Қаскөйлердің қозғалысы
        enemy_x = move_enemy(enemy_x, enemy_y)

        # Ойыншы мен қаскөйдің соқтығысуын тексеру
        if (player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2 < (player_radius + enemy_height // 2) ** 2:
            game_over = True  # Егер соқтығысса, ойын аяқталады

        # Экранды жаңарту
        screen.fill(BLACK)  # Экранды қара түспен толтыру
        draw_player(player_x, player_y)  # Ойыншының допты салу
        draw_enemy(enemy_x, enemy_y)  # Қаскөйді салу

        # Экранды жаңарту
        pygame.display.update()

        # FPS басқару
        clock.tick(60)

    # Ойын аяқталғанда хабарлама көрсету
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
    pygame.display.update()
    pygame.time.wait(2000)  # Хабарламаны 2 секунд көрсету

    pygame.quit()  # Pygame-ды тоқтату

# Негізгі функцияны бастау
main()
