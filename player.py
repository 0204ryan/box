import pygame
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x2 = self.x + 5
        self.y2 = self.y + 15

    def draw(self, screen, black, red):
        pygame.draw.ellipse(screen, black, [1 + self.x, self.y, 10, 10], 0)
        
        pygame.draw.line(screen, black, [5 + self.x, 17 + self.y], [10 + self.x, 27 + self.y], 2)
        pygame.draw.line(screen, black, [5 + self.x, 17 + self.y], [self.x, 27 + self.y], 2)
        
        pygame.draw.line(screen, red, [5 + self.x, 17 + self.y], [5 + self.x, 7 + self.y], 2)
        
        pygame.draw.line(screen, red, [5 + self.x, 7 + self.y], [9 + self.x, 17 + self.y], 2)
        pygame.draw.line(screen, red, [5 + self.x, 7 + self.y], [1 + self.x, 17 + self.y], 2)


    def move(self):
        pos = pygame.mouse.get_pos()
        self.y = pos[1]  
        self.x2 = self.x + 5
        self.y2 = self.y + 15