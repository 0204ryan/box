import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('heli.png')
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 0

    def update(self):
        self.speed_y += 0.2
        if self.rect.y >= 0:
            self.rect.y += self.speed_y
        else:
            self.rect.y = 0
        print(self.speed_y, self.rect.y)
        