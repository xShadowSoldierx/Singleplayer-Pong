import pygame
import random


pygame.init()
game_W = 500
game_H = 500
screen = pygame.display.set_mode([game_W, game_H])

rect_W = 100
rect_H = 10
rect_X = 200
rect_Y = 490
rect_Speed = 1.7

circle_R = 50
circle_X = random.randint(circle_R, game_W)
circle_Y = 250
circle_Speed_X = .1
circle_Speed_Y = .05

pygame.key.set_repeat(1, 5)

running = True
while running:
    # Increase difficulty over time
    circle_Speed_Y *= 1.000075
    rect_Speed *= 1.000025
    
    # Collision
    rect_collision_start_X = rect_X
    rect_collision_end_X = rect_X + rect_W
    
    # Game control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if rect_X > 0:
                    rect_X -= rect_Speed
            if event.key == pygame.K_RIGHT:
                if rect_X < (game_W - rect_W):
                    rect_X += rect_Speed
    
    # Ball movement in x direction
    circle_X += circle_Speed_X
    if circle_X > (game_W - circle_R):
        circle_Speed_X = -circle_Speed_X
    elif circle_X < circle_R:
        circle_Speed_X = -circle_Speed_X
        
    # Ball movement in y direction
    circle_Y += circle_Speed_Y
    if circle_Y > (game_H - circle_R - rect_H):
        if circle_X >= rect_collision_start_X and circle_X <= rect_collision_end_X:
            circle_Speed_Y = -circle_Speed_Y
        else: break
    elif circle_Y < circle_R:
        circle_Speed_Y = -circle_Speed_Y

    screen.fill((255, 255, 255))
        
    pygame.draw.circle(screen, (0, 0, 255), (circle_X, circle_Y), circle_R)
    
    pygame.draw.rect(screen, (240, 0, 30), (rect_X, rect_Y, rect_W, rect_H))
    
    pygame.display.update()

pygame.quit()