import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('heli.png')
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.y = pos[1]  
        self.rect.y = pos[1]