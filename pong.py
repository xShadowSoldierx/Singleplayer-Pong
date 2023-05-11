import os
import random
import sys
import pygame

from Button import *


pygame.init()
GAME_W = 500
GAME_H = 500
SCREEN = pygame.display.set_mode([GAME_W, GAME_H], flags=pygame.SCALED, vsync=1)
FPS = 60
FONT = pygame.font.Font(os.path.join('src', 'fonts', 'PressStart2P-Regular.ttf'), 20)

clock = pygame.time.Clock()

FILE = os.path.abspath(__file__)
PATH = os.path.dirname(FILE)


class Rectangle():
    def __init__(self, height: float, width: float,
                 x_coordinate: float, y_coordinate: float,
                 color: tuple,
                 speed_x: float = 0.0, speed_y: float = 0.0):
        
        self.height = height
        self.width = width
        
        self.x = x_coordinate
        self.y = y_coordinate
        
        self.color = color
        
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def moving_x(self, direction: str = 'right'):
        if direction.lower() == 'right':
            self.x += self.speed_x
        elif direction.lower() == 'left':
            self.x -= self.speed_x

    def moving_y(self, direction: str = 'down'):
        if direction.lower() == 'down':
            self.y += self.speed_y
        elif direction.lower() == 'up':
            self.y -= self.speed_y


class Circle():
    def __init__(self, radius: float,
                 x_coordinate: float, y_coordinate: float,
                 color: tuple,
                 speed_x: float = 0, speed_y: float = 0):
        
        self.radius = radius
        
        self.x = x_coordinate
        self.y = y_coordinate
    
        self.color = color
        
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def moving_x(self, direction: str = 'right'):
        if direction.lower() == 'right':
            self.x += self.speed_x
        elif direction.lower() == 'left':
            self.x -= self.speed_x

    def moving_y(self, direction: str = 'down'):
        if direction.lower() == 'down':
            self.y += self.speed_y
        elif direction.lower() == 'up':
            self.y -= self.speed_y


def main ():
    main_menu()


def main_menu():
    pygame.mixer.music.unload()
    pygame.mixer.music.load(f'{PATH}/src/sounds/8_Bit_Menu_-_David_Renda.mp3')
    pygame.mixer.music.play()
    
    title_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 80)
    title_text = title_font.render(f'PONG', False, (248, 244, 234))
    
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (GAME_W // 2, GAME_H // 2 - 70)
        
    play_btn = Button(SCREEN, 200, 50, (150, GAME_H // 2 + 30), 'Play', FONT, (245, 80, 80), (248, 244, 234), (148,0,0), antialiasing=False)
    
    control_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 10)
    control_text = control_font.render('Press any key to start the game!', False, (248, 244, 234))
    
    control_text_rect = control_text.get_rect()
    control_text_rect.center = (GAME_W // 2, GAME_H - 100)
        
    
    running = True
    while running:
        SCREEN.fill((25,25,25))
        
        # Game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return game()
        
        SCREEN.blit(title_text, title_text_rect)        
        play_btn.draw()
        play_btn.click(game)
        SCREEN.blit(control_text, control_text_rect)

        pygame.display.update()
                
        clock.tick(FPS)


def options():
    pass


def game():
    pygame.mixer.music.unload()
    pygame.mixer.music.load(f'{PATH}/src/sounds/Retro_Platforming_-_David_Fesliyan.mp3')
    pygame.mixer.music.play()
    
    paddle = Rectangle(10, 100, 200, 490, (245, 80, 80), 4, 0) # 1.7
    circle = Circle(15, random.randint(15, GAME_W - 15), 250, (248, 244, 234), 6, 3)

    score = 0

    running = True
    while running:
        SCREEN.fill((25, 25, 25))
        
        # Increase difficulty over time
        circle.speed_y *= 1.00275
        paddle.speed_x *= 1.0015 # 1.000025
        
        # Collision
        paddle_collision_start_X = paddle.x
        paddle_collision_end_X = paddle.x + paddle.width
        
        # Game control
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if paddle.x > 0:
                paddle.moving_x(direction='left')
        if keys[pygame.K_RIGHT]:
            if paddle.x < (GAME_W - paddle.width):
                paddle.moving_x(direction='right')

        # Ball movement in x direction
        circle.moving_x(direction='right')
        if circle.x > (GAME_W - circle.radius):
            circle.speed_x = -(circle.speed_x)
        elif circle.x < circle.radius:
            circle.speed_x = -(circle.speed_x)
            
        # Ball movement in y direction
        circle.moving_y(direction='down')
        if circle.y > (GAME_H - circle.radius - paddle.height):
            if circle.x >= paddle_collision_start_X and circle.x <= paddle_collision_end_X:
                circle.speed_y = -(circle.speed_y)
                score += 1
            else:
                running = False                
        elif circle.y < circle.radius:
            circle.speed_y = -(circle.speed_y)
            
        pygame.draw.circle(SCREEN, circle.color, (circle.x, circle.y), circle.radius)
        
        pygame.draw.rect(SCREEN, paddle.color, (paddle.x, paddle.y, paddle.width, paddle.height))
        
        pygame.display.update()
        
        clock.tick(FPS)
    
    return game_over(score)


def game_over(score):
    # pygame.mixer.music.fadeout(4500)
    
    control_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 10)
    game_over_text = FONT.render(f'Game Over!', False, (248, 244, 234))
    score_text = FONT.render(f'Your score was {score}.', False, (248, 244, 234))
    control_m_text = control_font.render('[M] main menu', False, (248, 244, 234))
    control_esc_text = control_font.render('[Esc] close', False, (248, 244, 234))
    
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (GAME_W // 2, GAME_H // 2 - 50)
    
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (GAME_W // 2, GAME_H // 2 + 50)
    
    control_m_text_rect = control_m_text.get_rect()
    control_m_text_rect.top = (GAME_H - 30)
    control_m_text_rect.left = 20
    
    control_esc_text_rect = control_esc_text.get_rect()
    control_esc_text_rect.top = (GAME_H - 30)
    control_esc_text_rect.left = (GAME_W - control_esc_text_rect.width - 20)
    
    running = True
    while running:
        SCREEN.fill((25, 25, 25))
        
        # Game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return main_menu()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        SCREEN.blit(game_over_text, game_over_rect)
        SCREEN.blit(score_text, score_text_rect)
        SCREEN.blit(control_m_text, control_m_text_rect)
        SCREEN.blit(control_esc_text, control_esc_text_rect)
        
        pygame.display.update()
        
        clock.tick(FPS)    


def credits():
    pass


if __name__ == '__main__':
    main()