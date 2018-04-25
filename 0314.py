import pygame
import random
from box import Box
from player import Player
screen_size = [700, 500]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def music():
    pygame.mixer.music.load('piano.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.queue('piano.mp3')


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
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)
background_position = [0, 0]
bg0 = pygame.image.load("bg0.jpg").convert()
bg1 = pygame.image.load("bg1.jpg").convert()
box_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
c = 0
z = 0

player = Player(0, 0)
player_group.add(player)

game_over = False
done0 = False
done = False
music()
while not done0:
    # event 事件 (鍵盤敲擊, 滑鼠移動, 滑鼠按鍵..)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done0 = True
        # 畫面重新調整大小
        if event.type == pygame.VIDEORESIZE:
            # The main code that resizes the window:
            # (recreate the window with the new size)
            screen_size = (event.w, event.h)
            surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            # 背景圖 放大
            screen.blit(pygame.transform.scale(bg0, screen_size), (0, 0))
            pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done0 = True

    screen.blit(pygame.transform.scale(bg0, screen_size), (0, 0)) # 把背景圖畫出來
    font = pygame.font.Font('wt014.ttf', 100)
    text = font.render("方塊戰爭", True, BLACK)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2 - 120
    screen.blit(text, [text_x, text_y])

    button = pygame.Surface((200, 70)) # 按鈕
    button.fill(RED)
    button_rect = button.get_rect() # 取得這個按鈕的長方形

    button_x = screen.get_width() / 2 - button_rect.width / 2
    button_y = screen.get_height() / 2 - button_rect.height / 2 + 100
    b = screen.blit(button, [button_x, button_y])
    
    font2 = pygame.font.Font('wt014.ttf', 30)
    text2 = font2.render("開始遊戲", True, BLACK)
    text2_rect = text2.get_rect()
    text2_x = screen.get_width() / 2 - text2_rect.width / 2
    text2_y = screen.get_height() / 2 - text2_rect.height / 2 + 100
    screen.blit(text2, [text2_x, text2_y])


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if b.collidepoint(pos):
                done0 = True

    pygame.display.flip() 
    clock.tick(60)
    
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
            screen.blit(pygame.transform.scale(bg1, screen_size), (0, 0))
            pygame.display.flip()


    screen.blit(pygame.transform.scale(bg1, screen_size), (0, 0)) # 把背景圖畫出來
    # screen.blit(background_image, background_position)
    
    if not game_over:
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
        random_y_1 = random.randint(0, screen_size[1])
        random_y_2 = random.randint(0, screen_size[1])
        box1 = Box(screen_size[0], random_y_1, 1 + z, BLACK) # 產生箱子
        box2 = Box(screen_size[0], random_y_2, 1 + z, BLACK) # 產生箱子
        while box1.y < box2.y and box2.y < box1.y + box1.h: 
            box2 = Box(750, random_y_2, 1 + z, BLACK) # 產生箱子
        box_group.add(box1)
        box_group.add(box2)
        z += 0.1
        c = 0

    if game_over:
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
    else:
        box_group.update()
        box_group.draw(screen)

        player_group.update()
        player_group.draw(screen)


        if pygame.sprite.spritecollide(player, box_group, False):
            print('碰撞')
            game_over = True

    pygame.display.flip() 
    clock.tick(60)
pygame.quit()