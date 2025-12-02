import pygame               # pygame кітапханасын қосу
import time                 # Уақытты басқару үшін time кітапханасын қосу

# Pygame-ды инициализациялау
pygame.init()

# Экран өлшемдері
SCREEN_WIDTH = 640         # Экранның ені
SCREEN_HEIGHT = 480        # Экранның биіктігі

# Түстерді анықтау
WHITE = (255, 255, 255)    # Ақ түс
RED = (255, 0, 0)          # Қызыл түс
GREEN = (0, 255, 0)        # Жасыл түс
BLUE = (0, 0, 255)         # Көк түс
ORIGINAL_TRIANGLE_COLOR = (0, 255, 255)  # Бастапқы үшбұрыш түсі (сары)

# Экранды орнату
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Экран өлшемін орнату
pygame.display.set_caption("Rectangle and Triangle Game")  # Экран терезесінің атын орнату

# Ойыншының тікбұрышын анықтау
rect_width = 50            # Тікбұрыштың ені
rect_height = 30           # Тікбұрыштың биіктігі
rect_x = SCREEN_WIDTH // 2 - rect_width // 2  # Тікбұрыштың бастапқы X позициясы (орталықта)
rect_y = SCREEN_HEIGHT // 2 - rect_height // 2  # Тікбұрыштың бастапқы Y позициясы (орталықта)
rect_speed = 5             # Тікбұрыштың жылдамдығы

# Статикалық үшбұрышты анықтау
triangle_x = 200           # Үшбұрыштың бастапқы X позициясы
triangle_y = 150           # Үшбұрыштың бастапқы Y позициясы
triangle_size = 60         # Үшбұрыштың өлшемі

# Ойын айнымалылары
triangle_color = ORIGINAL_TRIANGLE_COLOR  # Үшбұрыштың бастапқы түсі
last_touch_time = 0          # Үшбұрышқа соңғы тиген уақыт
triangle_touch_duration = 2  # Үшбұрыш түсінің өзгеру уақыт аралығы (секундтармен)
rectangle_inside_window = True   # Тікбұрыштың терезенің ішінде екендігі туралы айнымалы

# FPS басқару үшін сағат орнату
clock = pygame.time.Clock()

# Негізгі ойын циклі
running = True
while running:
    screen.fill(WHITE)  # Экранды ақ түсімен толтыру
    
    # Оқиғаларды өңдеу
    for event in pygame.event.get():  # Барлық оқиғаларды тексеру
        if event.type == pygame.QUIT:  # Егер терезені жабу сұрауы болса
            running = False            # Циклды тоқтату және терезені жабу
    
    # Басылған пернелерді алу
    keys = pygame.key.get_pressed()  # Қандай пернелер басылғанын алу
    
    # Тікбұрышты жылжыту
    if keys[pygame.K_LEFT] and rect_x > 0:  # Солға жылжу
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < SCREEN_WIDTH - rect_width:  # Оңға жылжу
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y > 0:  # Жоғарыға жылжу
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y < SCREEN_HEIGHT - rect_height:  # Төменге жылжу
        rect_y += rect_speed

    # Тікбұрышты анықтау
    player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)  # Тікбұрыштың аймағын анықтау

    # Үшбұрышты анықтау (pygame.draw.polygon көмегімен)
    triangle_points = [
        (triangle_x, triangle_y),  # Үшбұрыштың бірінші нүктесі
        (triangle_x + triangle_size, triangle_y),  # Үшбұрыштың екінші нүктесі
        (triangle_x + triangle_size // 2, triangle_y - triangle_size)  # Үшбұрыштың үшінші нүктесі
    ]
    
    # Тікбұрыш пен үшбұрыштың соқтығысқанын тексеру
    if player_rect.colliderect(pygame.Rect(triangle_x, triangle_y - triangle_size, triangle_size, triangle_size)):
        # Егер соқтығысса, үшбұрыштың түсін қызылға өзгерту
        triangle_color = RED
        last_touch_time = time.time()  # Соңғы соқтығысқан уақытты жазу
    else:
        triangle_color = ORIGINAL_TRIANGLE_COLOR  # Егер соқтығыс болмаса, үшбұрыштың бастапқы түсіне оралу
    
    # Егер үшбұрышқа тигеннен кейін 2 секунд өткен болса, үшбұрыштың түсін қалпына келтіру
    if time.time() - last_touch_time >= triangle_touch_duration:
        triangle_color = ORIGINAL_TRIANGLE_COLOR

    # Тікбұрышты экранға салу (ойыншы)
    pygame.draw.rect(screen, BLUE, player_rect)  # Тікбұрышты көк түсімен салу

    # Үшбұрышты экранға салу
    pygame.draw.polygon(screen, triangle_color, triangle_points)  # Үшбұрышты салу

    # Экранды жаңарту
    pygame.display.update()

    # FPS бақылауы (екі ойын кадры арасында қанша уақыт өткенін реттеу)
    clock.tick(60)

# Pygame-ды тоқтату
pygame.quit()
