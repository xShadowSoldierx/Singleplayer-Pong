import os
import random
import sys
import pygame

from button import *
from circle import *
from rectangle import *


pygame.init()
GAME_W = 500
GAME_H = 500
SCREEN = pygame.display.set_mode([GAME_W, GAME_H], flags=pygame.SCALED, vsync=1)
FPS = 60
FONT = pygame.font.Font(os.path.join('src', 'fonts', 'PressStart2P-Regular.ttf'), 20)
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

FILE = os.path.abspath(__file__)
PATH = os.path.dirname(FILE)


def main ():
    main_menu()


def main_menu():
    pygame.display.set_caption('Pong - Main Menu')
    
    pygame.mixer.music.unload()
    pygame.mixer.music.load(f'{PATH}/src/sounds/8_Bit_Menu_-_David_Renda.mp3')
    pygame.mixer.music.play(loops=-1, start=0.5, fade_ms=1000)
    
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
                return options()
        
        SCREEN.blit(title_text, title_text_rect)        
        play_btn.draw()
        play_btn.click(options)
        SCREEN.blit(control_text, control_text_rect)

        pygame.display.update()
                
        clock.tick(FPS)


def options():
    pygame.display.set_caption('Pong - Options')
    
    options_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 45)
    options_text = options_font.render(f'DIFFICULTY', False, (248, 244, 234))
    options_text_rect = options_text.get_rect()
    options_text_rect.center = (GAME_W // 2, GAME_H // 2 - 100)
        
    easy_btn = Button(SCREEN, 200, 50, (150, GAME_H // 2 - 20), 'Easy', FONT,
                      (60,179,113), (248, 244, 234), (107,142,35), antialiasing=False)
    medium_btn = Button(SCREEN, 200, 50, (150, GAME_H // 2 + 40), 'Medium', FONT,
                        (255, 165, 0), (248, 244, 234), (255,127,80), antialiasing=False)
    hard_btn = Button(SCREEN, 200, 50, (150, GAME_H // 2 + 100), 'Hard', FONT,
                      (245, 80, 80), (248, 244, 234), (148, 0, 0), antialiasing=False)
    
    
    running = True
    while running:
        SCREEN.fill((25,25,25))
        
        # Game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.blit(options_text, options_text_rect)        
        easy_btn.draw()
        easy_btn.click(countdown, 'easy')
        
        medium_btn.draw()
        medium_btn.click(countdown, 'medium')
        
        hard_btn.draw()
        hard_btn.click(countdown, 'hard')

        pygame.display.update()
                
        clock.tick(FPS)


def countdown(difficulty):
    pygame.mixer.music.unload()
    
    match difficulty:
            case 'easy':
                pygame.display.set_caption('Pong - Easy mode')
                pygame.mixer.music.load(f'{PATH}/src/sounds/Retro_Platforming_-_David_Fesliyan.mp3')
                pygame.mixer.music.play(loops=-1)

            case 'medium':
                pygame.display.set_caption('Pong - Medium mode')
                pygame.mixer.music.load(f'{PATH}/src/sounds/A_Bit_Of_Hope_-_David_Fesliyan.mp3')
                pygame.mixer.music.play(loops=-1)

            case 'hard':
                pygame.display.set_caption('Pong - Hard mode')
                pygame.mixer.music.load(f'{PATH}/src/sounds/Boss_Time_-_David_Renda.mp3')
                pygame.mixer.music.play(loops=-1, start=1.4)
    
    
    number = 3
    
    countdown_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 80)
        
    countdown = True
    
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        countdown_text = countdown_font.render(f'{number}', False, (248, 244, 234))
        countdown_text_rect = countdown_text.get_rect()
        countdown_text_rect.center = (GAME_W // 2, GAME_H // 2)
        
        SCREEN.fill((25, 25, 25))
        SCREEN.blit(countdown_text, countdown_text_rect)
        
        pygame.display.update()
        
        if number == 'GO!':
            pygame.time.wait(500)
            return game(difficulty)
        else:
            number -= 1
        
        if number == 0:
            number = 'GO!'
        
        clock.tick(1.5)


def game(difficulty):
    hud_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 10)
    
    difficulty_text = hud_font.render(f'{difficulty.capitalize()} Mode', False, (248, 244, 234))
    difficulty_text_rect = difficulty_text.get_rect()
    difficulty_text_rect.right = GAME_W - 10
    difficulty_text_rect.top = 10
    
    paddle = Rectangle(10, 100, 200, 490, (245, 80, 80), 4, 0) # 1.7
    circle = Circle(15, random.randint(15, GAME_W - 15), 250, (248, 244, 234), 6, 3)

    score = 0
    
    running = True
    
    if difficulty == 'easy': circle.speed_y *= 1.5; paddle.speed_x *= 1.5
    
    while running:
        SCREEN.fill((25, 25, 25))
        
        score_text = hud_font.render(f'Score: {score}', False, (248, 244, 234))
        score_text_rect = score_text.get_rect()
        score_text_rect.left = 10
        score_text_rect.top = 10
        
        # Acceleration
        match difficulty:
            case 'medium':
                circle.speed_y *= 1.001075
                paddle.speed_x *= 1.000775
            case 'hard':
                circle.speed_y *= 1.00275
                paddle.speed_x *= 1.0015
               
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
        SCREEN.blit(score_text, score_text_rect)
        SCREEN.blit(difficulty_text, difficulty_text_rect)
        
        pygame.display.update()
        
        clock.tick(FPS)
    
    return game_over(score, difficulty)


def game_over(score, difficulty):
    pygame.display.set_caption('Pong - Game over')
    
    control_font = pygame.font.Font(f'{PATH}/src/fonts/PressStart2P-Regular.ttf', 10)
    game_over_text = FONT.render(f'Game Over!', False, (248, 244, 234))
    score_text = FONT.render(f'Your score was {score}', False, (248, 244, 234))
    difficulty_text = FONT.render(f'on {difficulty.upper()} mode.', False, (248, 244, 234))
    control_m_text = control_font.render('[M] main menu', False, (248, 244, 234))
    control_esc_text = control_font.render('[Esc] close', False, (248, 244, 234))
    
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (GAME_W // 2, GAME_H // 2 - 50)
    
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (GAME_W // 2, GAME_H // 2)
    
    difficulty_text_rect = difficulty_text.get_rect()
    difficulty_text_rect.center = (GAME_W // 2, GAME_H // 2 + 50)
    
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
        SCREEN.blit(difficulty_text, difficulty_text_rect)
        SCREEN.blit(control_m_text, control_m_text_rect)
        SCREEN.blit(control_esc_text, control_esc_text_rect)
        
        pygame.display.update()
        
        clock.tick(FPS)    


def credits():
    pass


if __name__ == '__main__':
    main()