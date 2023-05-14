class Rectangle(object):
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




