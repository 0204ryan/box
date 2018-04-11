import pygame
import random

screen_size = [700, 500]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
s = 10
score = 0
score_c = 0

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x2 = self.x + 5
        self.y2 = self.y + 15

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [1 + self.x, self.y, 10, 10], 0)
        
        pygame.draw.line(screen, BLACK, [5 + self.x, 17 + self.y], [10 + self.x, 27 + self.y], 2)
        pygame.draw.line(screen, BLACK, [5 + self.x, 17 + self.y], [self.x, 27 + self.y], 2)
        
        pygame.draw.line(screen, RED, [5 + self.x, 17 + self.y], [5 + self.x, 7 + self.y], 2)
        
        pygame.draw.line(screen, RED, [5 + self.x, 7 + self.y], [9 + self.x, 17 + self.y], 2)
        pygame.draw.line(screen, RED, [5 + self.x, 7 + self.y], [1 + self.x, 17 + self.y], 2)


    def move(self):
        pos = pygame.mouse.get_pos()
        self.y = pos[1]  
        self.x2 = self.x + 5
        self.y2 = self.y + 15


class Box:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.w = random.randint(10, 100)
        self.h = random.randint(10, 50)
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h
        self.speed = speed

    def draw(self):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.w, self.h], 0)

    def move(self):
        self.x -= self.speed
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h

def calc_score(score):
    return 'Score:' + str(score)

def check(player, box):
    top_left = player.x <= box.x <= player.x2 and player.y <= box.y <= player.y2
    bottom_right = player.x <= box.x2 <= player.x2 and player.y <= box.y2 <= player.y2
    if top_left or bottom_right:
        return True
    return False

pygame.init()

screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
background_position = [0, 0]
background_image = pygame.image.load("bg1.jpg").convert()
boxes = []
c = 0
z = 0

player = Player(0, 0)

while not done:
    # event 事件 (鍵盤敲擊, 滑鼠移動, 滑鼠按鍵..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # 畫面重新調整大小
        if event.type == pygame.VIDEORESIZE:
            # The main code that resizes the window:
            # (recreate the window with the new size)
            screen_size = (event.w, event.h)
            surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            # 背景圖 放大
            screen.blit(pygame.transform.scale(background_image, screen_size), (0, 0))
            pygame.display.flip()


    screen.blit(pygame.transform.scale(background_image, screen_size), (0, 0)) # 把背景圖畫出來
    # screen.blit(background_image, background_position)
    
    score_c += 1
    if score_c > 20:
        score += 1
        score_c = 0

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(calc_score(score), True, BLACK)
    screen.blit(text, [0, 0])

    c += 1
    total = 200 - s 
    if total > 50:
        s += 0.02
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]   
    if c > total:                                 
        boxes.append(Box(700, y, 1 + z))
        boxes.append(Box(750, y, 1 + z))
        z += 0.5
        c = 0    
    for box in boxes:
        box.draw()
        box.move()
    player.move()
    player.draw()

    for box in boxes:
        重疊 = check(player, box)
        if 重疊: 
            print('失敗')

    pygame.display.flip() 
    clock.tick(60)
pygame.quit()