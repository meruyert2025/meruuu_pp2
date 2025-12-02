import pygame               # pygame кітапханасын қосу
import math                 # математикалық функциялар үшін math кітапханасын қосу

def main():
    pygame.init()  # Pygame-ды инициализациялау
    screen = pygame.display.set_mode((640, 480))  # Экран өлшемдерін орнату (640x480 пиксель)
    clock = pygame.time.Clock()  # FPS бақылаушы

    # --- Негізгі параметрлер ---
    brush_radius = 5  # Қылқаламның радиусы
    shape_thickness = 3  # Фигуралардың сызық қалыңдығы
    mode = 'blue'  # Бастапқы түс - көк
    tool = 'brush'  # Бастапқы құрал - қылқалам (brush)
    points = []  # Қылқаламмен сызықтар үшін нүктелер тізімі
    drawing = False  # Сурет салу жағдайы
    start_pos = (0, 0)  # Сурет салудың бастапқы позициясы

    # Түстердің анықтамасы
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255)
    }

    # Фонды жасаймыз (ақ фон)
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    while True:
        pressed = pygame.key.get_pressed()  # Пернелердің басылғанын алу
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  # ALT пернесі басылғанын тексеру
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  # CTRL пернесі басылғанын тексеру

        # Оқиғаларды өңдеу
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Егер терезе жабылса
                return
            if event.type == pygame.KEYDOWN:  # Егер перне басылса
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):  # ESC пернесі немесе ALT+F4 арқылы шығу
                    return

                # Түстерді өзгерту
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:
                    mode = 'black'
                elif event.key == pygame.K_w:
                    mode = 'white'

                # Құралдарды өзгерту (қосымша фигуралармен)
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                elif event.key == pygame.K_5:
                    tool = 'square'
                elif event.key == pygame.K_6:
                    tool = 'right_triangle'
                elif event.key == pygame.K_7:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_8:
                    tool = 'rhombus'

            # Тышқан оқиғаларын өңдеу
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Сол жақ кнопка басылса
                    drawing = True  # Сурет салу басталды
                    start_pos = event.pos  # Бастапқы позицияны алу
                    if tool in ['brush', 'eraser']:  # Егер құрал қылқалам немесе өшіргіш болса, нүктелерді қосу
                        points.append(start_pos)
                elif event.button == 3:  # Оң жақ кнопка басылса
                    brush_radius = max(1, brush_radius - 1)  # Қылқаламның радиусын кішірейту

            if event.type == pygame.MOUSEBUTTONUP:  # Тышқанды босату
                if event.button == 1 and drawing:  # Егер сол жақ тышқан басылса және сурет салу аяқталса
                    end_pos = event.pos  # Соңғы позицияны алу
                    color = colors[mode]  # Түсті таңдау

                    # Сурет салу (бар фигуралар)
                    if tool == 'rectangle':  # Тіктөртбұрыш салу
                        rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.rect(background, color, rect, shape_thickness)
                    elif tool == 'circle':  # Шеңбер салу
                        radius_c = int(math.hypot(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.circle(background, color, start_pos, radius_c, shape_thickness)

                    # Жаңа фигуралар
                    elif tool == 'square':  # Квадрат салу
                        side = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        rect = pygame.Rect(start_pos, (side if end_pos[0] >= start_pos[0] else -side,
                                                       side if end_pos[1] >= start_pos[1] else -side))
                        pygame.draw.rect(background, color, rect, shape_thickness)

                    elif tool == 'right_triangle':  # Тік бұрышты үшбұрыш салу
                        triangle_points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
                        pygame.draw.polygon(background, color, triangle_points, shape_thickness)

                    elif tool == 'equilateral_triangle':  # Тең бүйірлі үшбұрыш салу
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        height = abs(dx) * math.sqrt(3)/2
                        if dy < 0:
                            height = -height
                        triangle_points = [start_pos, (start_pos[0]+dx, start_pos[1]), (start_pos[0]+dx/2, start_pos[1]+height)]
                        pygame.draw.polygon(background, color, triangle_points, shape_thickness)

                    elif tool == 'rhombus':  # Ромб салу
                        dx = end_pos[0]-start_pos[0]
                        dy = end_pos[1]-start_pos[1]
                        rhombus_points = [
                            (start_pos[0], start_pos[1]-dy//2),
                            (start_pos[0]+dx//2, start_pos[1]),
                            (start_pos[0], start_pos[1]+dy//2),
                            (start_pos[0]-dx//2, start_pos[1])
                        ]
                        pygame.draw.polygon(background, color, rhombus_points, shape_thickness)

                    drawing = False  # Сурет салу аяқталды
                    points = []  # Нүктелер тізімін тазалау

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool in ['brush', 'eraser']:  # Қылқаламмен немесе өшіргішпен сурет салу
                    pos = event.pos
                    points.append(pos)
                    points = points[-256:]  # Нүктелердің санын шектеу

        screen.blit(background, (0, 0))  # Фонды экранға шығару
        color_value = colors[mode]  # Түсті таңдау

        # Қылқаламмен немесе өшіргішпен сурет салу
        if tool in ['brush', 'eraser']:
            draw_lines(screen, points, brush_radius, color_value if tool == 'brush' else (255, 255, 255))

        # Тікбұрыш, шеңбер және жаңа фигуралар алдын ала көрсетілімін салу
        if drawing and tool in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
            current_pos = pygame.mouse.get_pos()
            preview_color = colors[mode]
            if tool == 'rectangle':  # Алдын ала тікбұрыш көрсету
                rect = pygame.Rect(start_pos, (current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'circle':  # Алдын ала шеңбер көрсету
                radius_c = int(math.hypot(current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                pygame.draw.circle(screen, preview_color, start_pos, radius_c, shape_thickness)
            elif tool == 'square':  # Алдын ала квадрат көрсету
                side = max(abs(current_pos[0]-start_pos[0]), abs(current_pos[1]-start_pos[1]))
                rect = pygame.Rect(start_pos, (side if current_pos[0] >= start_pos[0] else -side,
                                               side if current_pos[1] >= start_pos[1] else -side))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'right_triangle':  # Алдын ала тікбұрышты үшбұрыш көрсету
                triangle_points = [start_pos, (current_pos[0], start_pos[1]), current_pos]
                pygame.draw.polygon(screen, preview_color, triangle_points, shape_thickness)
            elif tool == 'equilateral_triangle':  # Алдын ала тең бүйірлі үшбұрыш көрсету
                dx = current_pos[0] - start_pos[0]
                height = abs(dx) * math.sqrt(3)/2
                if current_pos[1] < start_pos[1]:
                    height = -height
                triangle_points = [start_pos, (start_pos[0]+dx, start_pos[1]), (start_pos[0]+dx/2, start_pos[1]+height)]
                pygame.draw.polygon(screen, preview_color, triangle_points, shape_thickness)
            elif tool == 'rhombus':  # Алдын ала ромб көрсету
                dx = current_pos[0]-start_pos[0]
                dy = current_pos[1]-start_pos[1]
                rhombus_points = [
                    (start_pos[0], start_pos[1]-dy//2),
                    (start_pos[0]+dx//2, start_pos[1]),
                    (start_pos[0], start_pos[1]+dy//2),
                    (start_pos[0]-dx//2, start_pos[1])
                ]
                pygame.draw.polygon(screen, preview_color, rhombus_points, shape_thickness)

        pygame.display.flip()  # Экранды жаңарту
        clock.tick(60)  # FPS-ты 60-қа орнату

# Сызықтарды салу функциясы
def draw_lines(screen, points, width, color):
    for i in range(len(points)-1):
        pygame.draw.line(screen, color, points[i], points[i+1], width)

# Негізгі функцияны шақыру
def new_func(main):
    main()

new_func(main)  # Ойынның негізгі циклін бастау
