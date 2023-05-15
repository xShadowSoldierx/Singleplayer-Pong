import pygame

class Button(object):    
    def __init__(self, main_window: object,
                 width: float, height: float, position: tuple,
                 content: str, font: object,
                 button_color: str | tuple, content_color: str | tuple,
                 hover_color: str | tuple = None, content_hover_color: str | tuple = None,
                 antialiasing:bool = True, border_radius: int = 0):
        
        # Core
        self.main_window = main_window

        # Button
        self.button_default_color = button_color
        self.button_color = button_color
        self.button_hover_color = hover_color
        self.button_rect = pygame.Rect(position, (width, height))
        
        self.border_radius = border_radius

        # Content
        self.content = content
        self.font = font
        self.antialiasing = antialiasing

        self.content_default_color = content_color
        self.content_color = content_color
        self.content_hover_color = content_hover_color
        self.content_surf = self.font.render(self.content, self.antialiasing, self.content_color)
        self.content_rect = self.content_surf.get_rect(center = self.button_rect.center)

        # Interactions
        self.pressed = False

    def draw(self):
        pygame.draw.rect(self.main_window, self.button_color, self.button_rect, border_radius = self.border_radius)
        self.main_window.blit(self.content_surf, self.content_rect)

    def click(self, func, *args, **kwargs):
        mouse_position = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_position):
            if self.button_hover_color:
                self.button_color = self.button_hover_color
            if self.content_hover_color:
                self.content_color = self.content_hover_color
                self.content_surf = self.font.render(self.content, self.antialiasing, self.content_color)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            elif self.pressed:
                func(*args, **kwargs)
                self.pressed = False
        else:
            self.button_color = self.button_default_color
            self.content_color = self.content_default_color
            self.content_surf = self.font.render(self.content, self.antialiasing, self.content_color)