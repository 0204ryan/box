import pygame
import random
from box import Box
from player import Player
from save import save_score, read_score
from heli import Heli

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


def score_max(max_score):
    return 'Max Score:' + str(max_score)


class Game:
    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.bg0 = pygame.image.load("bg0.jpg").convert()
        self.bg1 = pygame.image.load("bg1.jpg").convert()
        self.done = False
        self.intro_done = False # 開始畫面還沒結束!!!
        self.max_score = read_score()
        self.asd = 0
        self.restart()

    def process_events(self):
        # event 事件 (鍵盤敲擊, 滑鼠移動, 滑鼠按鍵..)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            # 畫面重新調整大小
            if event.type == pygame.VIDEORESIZE:
                # The main code that resizes the window:
                # (recreate the window with the new size)
                self.screen_size = (event.w, event.h)
                surface = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                # 背景圖 放大
                self.screen.blit(pygame.transform.scale(self.bg0, self.screen_size), (0, 0))
                pygame.display.flip()
            if event.type == pygame.KEYDOWN: # enter
                if event.key == pygame.K_RETURN:
                    self.intro_done = True

    def add_score(self):
        self.score_c += 1
        if self.score_c > 20:
            self.score += 1
            self.score_c = 0

    def game_logic(self):

        if not self.game_over:
            self.add_score()

        self.c += 1
        total = 200 - self.s
        if total > 50:
            self.s += 0.02

        if self.c > total:
            random_y_1 = random.randint(0, self.screen_size[1])
            random_y_2 = random.randint(0, self.screen_size[1])
            box1 = Box(self.screen_size[0], random_y_1, 1 + self.z, BLACK) # 產生箱子
            box2 = Box(self.screen_size[0], random_y_2, 1 + self.z, BLACK) # 產生箱子
            while box1.rect.colliderect(box2.rect): # 如果重疊，重新產生box2
                random_y_2 = random.randint(0, self.screen_size[1])
                box2 = Box(self.screen_size[0], random_y_2, 1 + self.z, BLACK) # 產生箱子
            self.box_group.add(box1)
            self.box_group.add(box2)
            self.z += 0.1
            self.c = 0

    def restart(self):
        self.save_done = False
        self.game_over = False
        self.score = 0
        self.c = 0
        self.z = 0
        self.s = 10
        self.score_c = 0
        self.ccccc = 0
        self.player_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.player = Player(0, 0)
        self.player_group.add(self.player)
        asd = 0

    def display_frame(self):
        self.screen.blit(pygame.transform.scale(self.bg1, self.screen_size), (0, 0)) # 把背景圖畫出來
        # screen.blit(background_image, background_position)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(calc_score(self.score), True, BLACK)
        self.screen.blit(text, [0, 0])

        if self.game_over:
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect()
            text_x = self.screen.get_width() / 2 - text_rect.width / 2
            text_y = self.screen.get_height() / 2 - text_rect.height / 2
            self.screen.blit(text, [text_x, text_y])

            if not self.save_done:
                if self.score > self.max_score:
                    save_score(self.score)
                    self.max_score = self.score
                    self.save_done = True

        else:
            self.box_group.update()

            self.box_group.draw(self.screen)

            self.player_group.update()
            self.player_group.draw(self.screen)

            if pygame.sprite.spritecollide(self.player, self.box_group, False):
                self.game_over = True

        pygame.display.flip()

    def display_choose(self):
        self.screen.blit(pygame.transform.scale(self.bg0, self.screen_size), (0, 0)) # 把背景圖畫出來
        font = pygame.font.Font('wt014.ttf', 60)
        text = font.render("選擇玩家", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])

        # 顯示圖片
        h0 = Heli(200, 200, 'ZF2.png')
        self.screen.blit(h0.image, h0.rect)

        button = pygame.Surface((200, 70)) # 按鈕
        button.fill(RED)
        button_rect = button.get_rect() # 取得這個按鈕的長方形

        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 100
        b = self.screen.blit(button, [button_x, button_y])
        
        font2 = pygame.font.Font('wt014.ttf', 30)
        text2 = font2.render("確認", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 100
        self.screen.blit(text2, [text2_x, text2_y])
        font3 = pygame.font.SysFont('Calibri', 30, True, False)
        text3 = font3.render(score_max(self.max_score), True, BLACK)
        self.screen.blit(text3, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if b.collidepoint(pos):
                    self.intro_done = True
                    self.restart()
                    break

        pygame.display.flip()

    def display_game_over(self):
        self.screen.blit(pygame.transform.scale(self.bg0, self.screen_size), (0, 0)) # 把背景圖畫出來
        font = pygame.font.Font('wt014.ttf', 60)
        text = font.render("遊戲結束", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])

        button = pygame.Surface((200, 70)) # 按鈕
        button.fill(RED)
        button_rect = button.get_rect() # 取得這個按鈕的長方形

        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 100
        b = self.screen.blit(button, [button_x, button_y])
        
        font2 = pygame.font.Font('wt014.ttf', 30)
        text2 = font2.render("重新開始", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 100
        self.screen.blit(text2, [text2_x, text2_y])
        font3 = pygame.font.SysFont('Calibri', 30, True, False)
        text3 = font3.render(score_max(self.max_score), True, BLACK)
        self.screen.blit(text3, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if b.collidepoint(pos):
                    self.intro_done = True
                    self.restart()
                    break

        pygame.display.flip()

    def display_intro(self):
        self.screen.blit(pygame.transform.scale(self.bg0, self.screen_size), (0, 0)) # 把背景圖畫出來
        font = pygame.font.Font('wt014.ttf', 100)
        text = font.render("方塊戰爭", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])

        button = pygame.Surface((200, 70)) # 按鈕
        button.fill(RED)
        button_rect = button.get_rect() # 取得這個按鈕的長方形

        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 100
        b = self.screen.blit(button, [button_x, button_y])
        
        font2 = pygame.font.Font('wt014.ttf', 30)
        text2 = font2.render("開始遊戲", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 100
        self.screen.blit(text2, [text2_x, text2_y])
        font3 = pygame.font.SysFont('Calibri', 30, True, False)
        text3 = font3.render(score_max(self.max_score), True, BLACK)
        self.screen.blit(text3, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if b.collidepoint(pos):
                    self.intro_done = True
                    break

        pygame.display.flip() 


def main():

    pygame.init()

    screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    pygame.display.set_caption("方塊戰爭")
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    background_position = [0, 0]

    music()
    g = Game(screen, screen_size) # 做出一個Game class的物件
    while True:
        g.process_events()

        if g.done: 
            break

        if g.intro_done == False:
            g.display_choose()
        elif g.game_over:
            g.display_game_over()
        else:
            g.game_logic()
            g.display_frame()

        clock.tick(60)

    pygame.quit()


main()