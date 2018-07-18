import pygame
class Heli(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (120, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        pos = pygame.mouse.get_pos()
        self.y = pos[1]
        self.rect.y = pos[1]
        
