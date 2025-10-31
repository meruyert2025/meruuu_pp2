
import pygame
import datetime

pygame.init()

W, H = 800, 800
center_x = W // 2  
center_y = H // 2  
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))

mickey = pygame.image.load("/Users/meruert/Desktop/base_micky.jpg")
secondHand = pygame.image.load("/Users/meruert/Downloads/second.png")
minuteHand = pygame.image.load("/Users/meruert/Downloads/minute.png")
mickeyRect = mickey.get_rect()


def rotate_and_blit(surface, image, center_point, rotation_angle):
    rotated_image = pygame.transform.rotate(image, rotation_angle)  
    image_rect = rotated_image.get_rect(center=image.get_rect(center=center_point).center)  
    surface.blit(rotated_image, image_rect)  

minute_angle = 0  
second_angle = 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    t = datetime.datetime.now()  
    minute_angle = (int(t.strftime('%M')) * 6) - 90  
    second_angle = (int(t.strftime('%S')) * 6) - 90  

    sc.fill(WHITE)
    sc.blit(mickey, (center_x - mickey.get_width() // 2, center_y - mickey.get_height() // 2))  
    
    rotate_and_blit(sc, secondHand, (center_x, center_y), -second_angle)  
    rotate_and_blit(sc, minuteHand, (center_x, center_y), -minute_angle) 

    pygame.display.update()
