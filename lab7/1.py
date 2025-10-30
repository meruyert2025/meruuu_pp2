
import pygame
import math
import datetime
import sys

pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


base = pygame.image.load(r"/Users/meruert/Desktop/base_micky.jpg").convert_alpha()
minute_hand = pygame.image.load(r"/Users/meruert/Downloads/minute.png").convert_alpha()
second_hand = pygame.image.load(r"/Users/meruert/Downloads/second.png").convert_alpha()


base = pygame.transform.smoothscale(base, (WIDTH, HEIGHT))


CENTER = (WIDTH // 2, HEIGHT // 2)


clock = pygame.time.Clock()
running = True

def rotate_center(image, angle):
    """Вращает изображение вокруг центра"""
    rotated_image = pygame.transform.rotozoom(image, -angle, 1)
    rotated_rect = rotated_image.get_rect(center=CENTER)
    return rotated_image, rotated_rect

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = datetime.datetime.now()
    second = now.second + now.microsecond / 1_000_000  
    minute = now.minute + second / 60

    
    second_angle = second * 6           
    minute_angle = minute * 6           

    
    screen.fill((255, 255, 255))
    screen.blit(base, (0, 0))

    
    rotated_minute, rect_minute = rotate_center(minute_hand, minute_angle)
    rotated_second, rect_second = rotate_center(second_hand, second_angle)

    screen.blit(rotated_minute, rect_minute)
    screen.blit(rotated_second, rect_second)

    pygame.display.flip()
    clock.tick(60)  
pygame.quit()
sys.exit()