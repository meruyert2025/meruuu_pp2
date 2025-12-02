import pygame               # pygame кітапханасын қосу
import random               # Кездейсоқ сандарды жасау үшін random кітапханасын қосу

pygame.init()               # Pygame-ды инициализациялау

# --- Экран параметрлері ---
WIDTH, HEIGHT = 500, 600    # Экранның ені мен биіктігін орнату
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран терезесін жасау
pygame.display.set_caption("Поймай треугольники")  # Терезенің атын орнату

# --- Платформаның параметрлері (ойыншы) ---
platform_width = 120        # Платформаның ені
platform_height = 20        # Платформаның биіктігі
platform_x = WIDTH // 2 - platform_width // 2  # Платформаның бастапқы X позициясы (орталықта)
platform_y = HEIGHT - 40    # Платформаның бастапқы Y позициясы (экранның төменгі жағында)
platform_speed = 6          # Платформаның жылдамдығы

# --- Падающие треугольники ---
triangles = []              # Барлық үшбұрыштар тізімін анықтау
triangle_speed = 4          # Үшбұрыштың құлау жылдамдығы
spawn_delay = 40            # Әр 40 кадрда жаңа үшбұрыш пайда болады

# --- Счёт ---
score = 0                   # Ойыншының ұпайы
font = pygame.font.SysFont("Arial", 28)  # Шрифт орнату

clock = pygame.time.Clock()  # FPS бақылаушы сағат
running = True               # Ойынның жұмыс істейтінін бақылау
frame = 0                    # Кадрларды санау

while running:
    clock.tick(60)           # FPS-ты 60 кадрға шектеу
    frame += 1               # Кадрлар санын арттыру

    for event in pygame.event.get():  # Барлық оқиғаларды өңдеу
        if event.type == pygame.QUIT:  # Егер терезе жабылса
            running = False           # Циклды тоқтату

    # --- Платформаны басқару ---
    keys = pygame.key.get_pressed()  # Қандай пернелер басылғанын алу
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and platform_x > 0:  # Солға жылжыту
        platform_x -= platform_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and platform_x < WIDTH - platform_width:  # Оңға жылжыту
        platform_x += platform_speed

    # --- Жаңа үшбұрыштарды жасау ---
    # Әр 40 кадр сайын кездейсоқ орындағы жаңа үшбұрышты жасау
    if frame % spawn_delay == 0:
        new_x = random.randint(20, WIDTH - 20)  # Кездейсоқ X орнын анықтау
        triangles.append({"x": new_x, "y": -20})  # Үшбұрышты жоғарғы жағынан қосу

    # --- Үшбұрыштардың қозғалысы және соқтығысуды тексеру ---
    for t in triangles[:]:           # Тізімнің көшірмесін қолдану
        t["y"] += triangle_speed     # Үшбұрышты төменге жылжыту

        # Егер үшбұрыш экранның төменгі шекарасына жетсе, оны жою
        if t["y"] > HEIGHT:
            triangles.remove(t)      # Үшбұрышты жою
            continue

        # Платформа үшбұрышты ұстады ма? Тексеру
        if (platform_y <= t["y"] + 20 <= platform_y + platform_height) and \
           (platform_x <= t["x"] <= platform_x + platform_width):
            score += random.randint(1, 3)  # Случайлық ұпайларды қосу (1 мен 3 арасында)
            triangles.remove(t)            # Ұсталған үшбұрышты жою

    # --- Графика салу ---
    win.fill((20, 20, 20))          # Экранның фонын қою түске бояу

    # Платформаны салу
    pygame.draw.rect(win, (0, 150, 250),  # Платформаны көк түсімен салу
                     (platform_x, platform_y, platform_width, platform_height))

    # Падающие үшбұрыштарды салу
    for t in triangles:
        points = [
            (t["x"], t["y"]),           # Үшбұрыштың жоғарғы нүктесі
            (t["x"] - 15, t["y"] + 30), # Сол жақ төменгі нүктесі
            (t["x"] + 15, t["y"] + 30)  # Оң жақ төменгі нүктесі
        ]
        pygame.draw.polygon(win, (255, 200, 0), points)  # Үшбұрышты сары түспен салу

    # Счётты экранда көрсету
    text = font.render(f"Счёт: {score}", True, (255, 255, 255))  # Счёт мәтінін жасау
    win.blit(text, (10, 10))         # Счётты экранның жоғарғы сол жағына орналастыру

    pygame.display.update()          # Экранды жаңарту

pygame.quit()  # Ойын аяқталған соң pygame-ды тоқтату
