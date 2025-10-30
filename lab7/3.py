import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Move")


WHITE = (255, 255, 255)
RED = (220, 20, 60)


RADIUS = 25
STEP = 20  


x, y = WIDTH // 2, HEIGHT // 2


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        elif event.type == pygame.KEYDOWN:
            nx, ny = x, y  
            if event.key == pygame.K_UP:
                ny -= STEP  
            elif event.key == pygame.K_DOWN:
                ny += STEP  
            elif event.key == pygame.K_LEFT:
                nx -= STEP  
            elif event.key == pygame.K_RIGHT:
                nx += STEP  

            
            if RADIUS <= nx <= WIDTH - RADIUS and RADIUS <= ny <= HEIGHT - RADIUS:
                x, y = nx, ny

   
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (x, y), RADIUS)

    
    pygame.display.flip()

    
    clock.tick(60)


pygame.quit()
sys.exit()
