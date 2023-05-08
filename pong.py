import pygame
import random


pygame.init()
GAME_W = 500
GAME_H = 500
SCREEN = pygame.display.set_mode([GAME_W, GAME_H])

pygame.key.set_repeat(1, 5)

clock = pygame.time.Clock()


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


def main (GAME_W, GAME_H):
    main_menu(GAME_W, GAME_H)


def main_menu(GAME_W, GAME_H):
    running = True
    while running:
        SCREEN.fill((25,25,25))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return game(GAME_W, GAME_H)
                
        clock.tick(60)


def options():
    pass


def game(GAME_W, GAME_H):
    pygame.mixer.music.load('src/sounds/Retro_Platforming_-_David_Fesliyan.mp3')
    pygame.mixer.music.play()
    
    paddle = Rectangle(10, 100, 200, 490, (245, 80, 80), 1.7, 0)
    circle = Circle(15, random.randint(15, GAME_W - 15), 250, (248, 244, 234), 6, 3)

    score = 0

    running = True
    while running:
        SCREEN.fill((25, 25, 25))
        # Increase difficulty over time
        circle.speed_y *= 1.00275 # 1.000075
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
    pygame.mixer.music.fadeout(5000)
    SCREEN.fill((25, 25, 25))
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Your score was: " + f'{score}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (GAME_W // 2, GAME_H // 2)
    SCREEN.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(5000)
    
    pygame.quit()


if __name__ == '__main__':
    main(GAME_W, GAME_H)