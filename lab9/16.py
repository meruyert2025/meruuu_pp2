import pygame               # pygame кітапханасын графика және оқиғалар үшін қосу
import random               # random кітапханасын кездейсоқ позициялар жасау үшін қосу

pygame.init()               # Барлық pygame модульдерін инициализациялау

# --- Экран параметрлері ---
WIDTH, HEIGHT = 800, 600    # Экранның ені мен биіктігін орнату
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран терезесін жасау
pygame.display.set_caption("Click the Rectangle!")  # Терезенің атауын орнату

# --- Тікбұрыштың параметрлері ---
rect_width, rect_height = 100, 60   # Тікбұрыштың өлшемдері
rect_x = WIDTH // 2 - rect_width // 2   # Горизонталь бойынша орталықта бастау
rect_y = HEIGHT // 2 - rect_height // 2 # Вертикаль бойынша орталықта бастау
rect_color = (255, 0, 0)             # Алғашқы тікбұрыш түсі (қызыл)

# --- Басу санын есептеу ---
clicks = 0                           # Басу санын 0-ден бастау
font = pygame.font.SysFont(None, 40) # Экранға мәтін көрсету үшін стандартты шрифт жүктеу

# --- Ойынның жұмыс істеу циклі ---
running = True                       # Ойын циклі жұмыс істеп тұруы үшін айнымалы

# --- Негізгі ойын циклі ---
while running:
    for event in pygame.event.get():  # Барлық оқиғаларды тексеру
        if event.type == pygame.QUIT: # Егер терезе жабылса
            running = False           # Циклды тоқтату және шығу

        if event.type == pygame.MOUSEBUTTONDOWN:  # Егер тышқан батырмасы басылса
            mouse_x, mouse_y = event.pos          # Нұқылған орынның координаттарын алу

            # Егер нұқу тікбұрыштың ішінде болса
            if (rect_x <= mouse_x <= rect_x + rect_width and
                rect_y <= mouse_y <= rect_y + rect_height):

                clicks += 1                       # Басу санын 1-ге көбейту

        if clicks==5:
            rect_width, rect_height = 100*2, 60*2
            rect_x = WIDTH // 2 - rect_width // 2   # Горизонталь бойынша орталықта бастау
            rect_y = HEIGHT // 2 - rect_height // 2 # Вертикаль бойынша орталықта бастау
        if clicks==10:
            rect_x +=50

            

        




    screen.fill((255, 255, 255))                 # Экранның фонын ақ түсімен толтыру

    pygame.draw.rect(screen, rect_color,         # Тікбұрышты салу
                     (rect_x, rect_y, rect_width, rect_height))

    # Басу санын экранда көрсету
    text_surface = font.render(f"Clicks: {clicks}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))          # Мәтінді экранның жоғарғы сол жағына орналастыру

    pygame.display.flip()                        # Экранды жаңарту

pygame.quit()                                    # Циклдан шыққан соң pygame-ды тоқтату

