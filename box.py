import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Box:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.w = random.randint(10, 100)
        self.h = random.randint(10, 50)
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h
        self.speed = speed

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, [self.x, self.y, self.w, self.h], 0)

    def move(self):
        self.x -= self.speed
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h

