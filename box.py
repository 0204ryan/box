import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.x = x
        self.y = y
        self.w = random.randint(10, 100)
        self.h = random.randint(10, 50)
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color)
        self.rect = self.image.get_rect() # 取得長方形
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

