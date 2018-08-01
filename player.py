import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_file, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (100, 45))
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        pos = list(pos)
        if pos[1] <= 0:
            pos[1] = 0
        if pos[1] >= self.screen.get_height() - 45:
            pos[1] = self.screen.get_height() - 45
        self.x = pos[0]
        self.y = pos[1]
        self.rect.x = pos[0]
        self.rect.y = pos[1]