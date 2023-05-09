import pygame
import os
import random


pygame.init()
GAME_W = 500
GAME_H = 500
SCREEN = pygame.display.set_mode([GAME_W, GAME_H])
FONT = pygame.font.Font(os.path.join('src', 'fonts', 'PressStart2P-Regular.ttf'), 20)

pygame.key.set_repeat(1, 5)

clock = pygame.time.Clock()


# class Button():
#     btn_color = (255, 0, 0)
#     hovor_color = (0, 255, 0)
#     click_color = (0, 0, 255)
#     font_color = (255, 255, 255)
    
#     height = 50
#     width = 100
    
#     def __init__(self, x_coordinate: float, y_coordinate: float, text: str):
#         self.x = x_coordinate
#         self.y = y_coordinate
#         self.text = text
        
#     def create_button(self):
#         global clicked
#         action = False
        
#         mouse_position = pygame.mouse.get_pos()
        
#         button_rectangle = pygame.Rect(self.x, self.y, self.height, self.width)
        
#         if button_rectangle.collidepoint(mouse_position):
#             if pygame.mouse.get_pressed()[0] ==  1:
#                 clicked = True
#                 pygame.draw.rect(SCREEN, self.click_color, button_rectangle)
#             elif pygame.mouse.get_pressed()[0] == 0 and clicked:
#                 clicked == False
#                 action = True
#             else:
#                 pygame.draw.rect(SCREEN, self.hover_color, button_rectangle)
#         else:
#             pygame.draw.rect(SCREEN, self.btn_color, button_rectangle)
            
#         btn_text = FONT.render(self.text, False, self.font_color)
#         btn_text_length = btn_text.get_width()
#         SCREEN.blit(btn_text, self.x + self.width / 2 - btn_text_length / 2, self.y + 5)
#         return action


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
    pygame.mixer.music.load('src/sounds/8_Bit_Menu_-_David_Renda.mp3')
    pygame.mixer.music.play()
    
    title_font = pygame.font.Font(os.path.join('src', 'fonts', 'PressStart2P-Regular.ttf'), 80)
    title_text = title_font.render(f'PONG', False, (248, 244, 234))
    
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (GAME_W // 2, GAME_H // 2 - 50)
    
    play_btn = Rectangle(50, 200, 150, GAME_H // 2 + 50, (245, 80, 80))
    
    play_btn_text = FONT.render(f'PLAY', False, (248, 244, 234))
    
    play_btn_text_rect = play_btn_text.get_rect()
    play_btn_text_rect.center = (GAME_W // 2, GAME_H // 2 + 75)
    
    # play_btn_2 = Button(300, 100, 'Test')
    
    running = True
    while running:
        SCREEN.fill((25,25,25))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return game()
        
        # play_btn_2.create_button()
        SCREEN.blit(title_text, title_text_rect)        
        pygame.draw.rect(SCREEN, play_btn.color, (play_btn.x, play_btn.y, play_btn.width, play_btn.height))
        SCREEN.blit(play_btn_text, play_btn_text_rect)

        pygame.display.update()
                
        clock.tick(60)


def options():
    pass


def game():
    pygame.mixer.music.load('src/sounds/Retro_Platforming_-_David_Fesliyan.mp3')
    pygame.mixer.music.play()
    
    paddle = Rectangle(10, 100, 200, 490, (245, 80, 80), 1.7, 0)
    circle = Circle(15, random.randint(15, GAME_W - 15), 250, (248, 244, 234), 6, 3)

    score = 0

    running = True
    while running:
        SCREEN.fill((25, 25, 25))
        # Increase difficulty over time
        circle.speed_y *= 1.00275
        paddle.speed_x *= 1.000025
        
        # Collision
        rect_collision_start_X = paddle.x
        rect_collision_end_X = paddle.x + paddle.width
        
        # Game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if paddle.x > 0:
                        paddle.moving_x(direction='left')
                if event.key == pygame.K_RIGHT:
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
            if circle.x >= rect_collision_start_X and circle.x <= rect_collision_end_X:
                circle.speed_y = -(circle.speed_y)
                score += 1
            else:
                running = False                
        elif circle.y < circle.radius:
            circle.speed_y = -(circle.speed_y)
            
        pygame.draw.circle(SCREEN, circle.color, (circle.x, circle.y), circle.radius)
        
        pygame.draw.rect(SCREEN, paddle.color, (paddle.x, paddle.y, paddle.width, paddle.height))
        
        pygame.display.update()
        
        clock.tick(60)
    
    return credits(score)


def credits(score):
    pygame.mixer.music.fadeout(4500)
    SCREEN.fill((25, 25, 25))
    game_over_text = FONT.render(f'Game Over!', False, (248, 244, 234))
    score_text = FONT.render(f'Your score was {score}.', False, (248, 244, 234))
    
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (GAME_W // 2, GAME_H // 2 - 50)
    
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (GAME_W // 2, GAME_H // 2 + 50)
    SCREEN.blit(game_over_text, game_over_rect)
    SCREEN.blit(score_text, score_text_rect)
    pygame.display.update()
    pygame.time.wait(5000)
    
    pygame.quit()


if __name__ == '__main__':
    main()