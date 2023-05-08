import pygame

import pygame
from random import randint

pygame.init()
game_W = 500
game_H = 500
screen = pygame.display.set_mode([game_W, game_H])

rect_X = 200
rect_Y = 490
rect_W = 100
rect_H = 10
rect_Speed = 1.25

circle_X = 250
circle_Y = 250
circle_R = 50
circle_Speed = .2


pygame.key.set_repeat(1, 5)

running = True
while running:
    rect_collision_start_X = rect_X
    rect_collision_end_X = rect_X + rect_W
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_X -= rect_Speed
            if event.key == pygame.K_RIGHT:
                rect_X += rect_Speed
    
    circle_X += circle_Speed
    
    # if circle_X > game_W - circle_R:
    #     circle_2_Speed = -circle_Speed
    # elif circle_X < circle_R / 2:
    #     circle_2_Speed = -circle_Speed

    screen.fill((255, 255, 255))
        
    pygame.draw.circle(screen, (0, 0, 255), (circle_X, circle_Y), circle_R)
    
    pygame.draw.rect(screen, (240, 0, 30), (rect_X, rect_Y, rect_W, rect_H))
    
    pygame.display.update()

pygame.quit()