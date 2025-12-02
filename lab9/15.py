#aisha
import pygame  # Pygame кітапханасын қосу
import random  # Кездейсоқ сандар үшін random кітапханасын қосу

# Pygame-ды инициализациялау
pygame.init()

# Экранның өлшемдері
WIDTH, HEIGHT = 640, 480  # Экранның ені мен биіктігі
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экранды орнату
pygame.display.set_caption("Coin Collector Game")  # Экранның атын орнату
clock = pygame.time.Clock()  # FPS бақылаушы

# Түстердің анықтамасы
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ойыншының тікбұрышының бастапқы параметрлері
player_width = 100  # Ойыншының тікбұрышының ені
player_height = 20  # Ойыншының тікбұрышының биіктігі
player_x = WIDTH // 2 - player_width // 2  # Бастапқы X позициясы
player_y = 50  # Ойыншының Y позициясы
player_speed = 5  # Ойыншының жылдамдығы

# Монетаның параметрлері
coin_radius = 10  # Монетаның радиусы
coin_x = player_x + player_width // 2  # Монетаның бастапқы X позициясы
coin_y = player_y  # Монетаның бастапқы Y позициясы
coin_falling = False  # Монетаның түсуін тексеретін айнымалы

# Ойынның параметрлері
score = 0  # Бастапқы ұпай
font = pygame.font.SysFont("Arial", 30)  # Шрифт орнату

# Ойынның негізгі циклі
running = True  # Ойынның жұмыс істейтінін бақылау
while running:
    clock.tick(60)  # FPS шектеу

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Егер терезе жабылса
            running = False  # Ойынды тоқтату

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Солға жылжыту
                if player_x > 0:
                    player_x -= player_speed  # Ойыншыны солға жылжыту
            elif event.key == pygame.K_RIGHT:  # Оңға жылжыту
                if player_x < WIDTH - player_width:
                    player_x += player_speed  # Ойыншыны оңға жылжыту

            if event.key == pygame.K_SPACE and not coin_falling:  # Егер SPACE басылса және монета әлі түспей жатса
                coin_falling = True  # Монетаның түсуін бастау
                coin_x = player_x + player_width // 2  # Монетаны ойыншының үстінен бастау
                coin_y = player_y  # Монетаның бастапқы Y позициясы

    if coin_falling:  # Монетаның түсуі
        coin_y += 5  # Монетаны төмен түсіру
        if coin_y > HEIGHT:  # Егер монета экранның төменгі шекарасына жетсе
            coin_falling = False  # Монетаны тоқтату
            score += 1  # Ұпайды 1-ге арттыру

    # Ойыншының тікбұрышының және монетаның экранда көрсетілуі
    screen.fill(WHITE)  # Экранды ақ түспен толтыру

    # Ойыншының тікбұрышы
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Монетаның түсуі
    if coin_falling:
        pygame.draw.circle(screen, RED, (coin_x, coin_y), coin_radius)  # Монетаны қызыл түспен салу

    # Ұпайды көрсету
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Ұпай мәтіні
    screen.blit(score_text, (10, 10))  # Ұпай мәтінін экранға шығару

    pygame.display.flip()  # Экранды жаңарту

pygame.quit()  # Pygame-ды тоқтату
