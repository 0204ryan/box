import pygame
import random
from box import Box # 從 box檔案中載入Box class
from player import Player

screen_size = [700, 500]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def calc_score(score):
    return 'Score:' + str(score)

def check(player, box):
    top_left = player.x <= box.x <= player.x2 and player.y <= box.y <= player.y2
    bottom_right = player.x <= box.x2 <= player.x2 and player.y <= box.y2 <= player.y2
    if top_left or bottom_right:
        return True
    return False


s = 10
score = 0
score_c = 0

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
        box.draw(screen, BLACK)
        box.move()
    player.move()
    player.draw(screen, BLACK, RED)

    for box in boxes:
        重疊 = check(player, box)
        if 重疊: 
            print('失敗')

    pygame.display.flip() 
    clock.tick(60)
pygame.quit()