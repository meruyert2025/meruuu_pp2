import pygame               # pygame кітапханасын қосу
import random               # random кітапханасын қосу (кездейсоқ сандар үшін)

pygame.init()               # Pygame-ды инициализациялау

# Экранның ені мен биіктігін орнату
WIDTH, HEIGHT = 600, 600   
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран терезесін жасау
pygame.display.set_caption("Triangle Collector")  # Терезенің атын орнату

# Ойыншының бастапқы параметрлері
player_x, player_y = WIDTH // 2, HEIGHT // 2  # Ойыншының бастапқы орнын орнату (экранның ортасы)
player_size = 30                    # Ойыншының өлшемі
speed = 5                           # Ойыншының жылдамдығы

# Кездейсоқ шеңбердің параметрлері
circle_x = random.randint(20, WIDTH - 20)  # Шеңбердің бастапқы X координаты
circle_y = random.randint(20, HEIGHT - 20)  # Шеңбердің бастапқы Y координаты
circle_r = 12                        # Шеңбердің радиусы

# Счёт
score = 0                            # Ұпайдың бастапқы мәні
font = pygame.font.SysFont(None, 40)  # Шрифт орнату

run = True  # Ойынның жұмыс істейтінін бақылау
while run:  # Ойын циклі
    pygame.time.delay(15)  # 15 миллисекундтық кідіріс (FPS басқару)

    for e in pygame.event.get():  # Барлық оқиғаларды өңдеу
        if e.type == pygame.QUIT:  # Егер терезе жабылса
            run = False  # Циклды тоқтату

    # Ойыншының қозғалысын басқару
    keys = pygame.key.get_pressed()  # Қандай пернелер басылғанын алу
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Солға жылжу
        player_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Оңға жылжу
        player_x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:  # Жоғары жылжу
        player_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Төмен жылжу
        player_y += speed

    # Экран шекараларын тексеру (ойыншы экраннан шықпасын)
    player_x = max(0, min(WIDTH - player_size, player_x))  # Сол жақ және оң жақ шекараларды тексеру
    player_y = max(0, min(HEIGHT - player_size, player_y))  # Жоғары және төмен шекараларды тексеру

    # Ойыншының шеңбермен соқтығысқанын тексеру
    # Екі нүктенің арасындағы қашықтықты есептеу
    dist = ((player_x + player_size // 2 - circle_x) ** 2 + (player_y + player_size // 2 - circle_y) ** 2) ** 0.5
    if dist < player_size // 2 + circle_r:  # Егер қашықтық шеңбердің радиусынан кіші болса
        score += random.randint(1, 5)  # Случайлық ұпайларды қосу (1 мен 5 арасында)
        # Жаңа шеңбердің орнын орнату
        circle_x = random.randint(20, WIDTH - 20)
        circle_y = random.randint(20, HEIGHT - 20)

    # Рисование
    win.fill((0, 0, 0))  # Экранды қара түспен толтыру

    # Ойыншыны үшбұрыш ретінде салу
    pygame.draw.polygon(win, (0, 200, 255), [
        (player_x + player_size // 2, player_y),  # Үшбұрыштың жоғарғы нүктесі
        (player_x, player_y + player_size),        # Сол жақ төменгі нүктесі
        (player_x + player_size, player_y + player_size)  # Оң жақ төменгі нүктесі
    ])

    # Шеңберді салу
    pygame.draw.circle(win, (255, 50, 50), (circle_x, circle_y), circle_r)  # Қызыл шеңбер салу

    # Счётты экранға көрсету
    win.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))  # Ұпайды экранға шығару

    pygame.display.update()  # Экранды жаңарту

pygame.quit()  # Oйын аяқталған соң pygame-ды тоқтату
