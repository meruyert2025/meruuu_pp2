import pygame               # pygame кітапханасын қосу
pygame.init()               # Pygame-ды инициализациялау

# Экранның ені мен биіктігін орнату
w = 800                    
h = 800
win = pygame.display.set_mode((w, h))  # Экран терезесін жасау

size = 50                    # Тікбұрыштың өлшемі
x = w // 2                   # Тікбұрыштың бастапқы X координаты (экран ортасында)
y = h // 2                   # Тікбұрыштың бастапқы Y координаты (экран ортасында)
speed = 5                    # Тікбұрыштың қозғалу жылдамдығы

font = pygame.font.SysFont(None, 30)  # Шрифт орнату

run = True  # Ойынның жұмыс істейтінін бақылау
while run:  # Ойын циклі
    for e in pygame.event.get():  # Барлық оқиғаларды өңдеу
        if e.type == pygame.QUIT:  # Егер терезе жабылса
            run = False           # Циклды тоқтату
        if e.type == pygame.KEYDOWN:  # Егер перне басылса
            if e.key == pygame.K_SPACE:  # Егер SPACE пернесі басылса
                x = w // 2           # Тікбұрышты экранның ортасына орналастыру
                y = h // 2

    keys = pygame.key.get_pressed()  # Қандай пернелер басылғанын алу

    # Тікбұрышты солға жылжыту
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  
        x -= speed

    # Тікбұрышты оңға жылжыту
    if keys[pygame.K_RIGHT] or keys[pygame.K_b]:  
        x += speed

    # Тікбұрышты жоғары жылжыту
    if keys[pygame.K_UP] or keys[pygame.K_d]:  
        y -= speed

    # Тікбұрышты төмен жылжыту
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:  
        y += speed

    # Экранның шекараларынан тысқа шығуды болдырмау
    if x < 0:  # Егер тікбұрыш экранның сол жағына шықса
        x = 0
    if y < 0:  # Егер тікбұрыш экранның жоғарғы жағына шықса
        y = 0
    if x + size > w:  # Егер тікбұрыш экранның оң жағына шықса
        x = w - size
    if y + size > h:  # Егер тікбұрыш экранның төменгі жағына шықса
        y = h - size

    win.fill((0, 0, 0))  # Экранның фонын қара түске бояу
    pygame.draw.rect(win, (255, 0, 0), (x, y, size, size))  # Қызыл тікбұрышты салу
    text = font.render("x-" + str(x) + ", y-" + str(y), True, (255, 255, 255))  # Координаттарды көрсету
    win.blit(text, (10, 10))  # Мәтінді экранға орналастыру
    pygame.display.update()  # Экранды жаңарту

pygame.quit()  # Pygame-ды тоқтату
