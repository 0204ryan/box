import pygame
import random
from box import Box
from player import Player
from db import Db
from heli import Heli
from pygame.locals import *
from sign import Sign

screen_size = [1000, 700]
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
        self.events = []
        self.background_sign_in = pygame.image.load("images/background.jpg").convert()
        self.background_game = pygame.image.load("images/background.jpg").convert()
        self.state = 'signin'
        self.done = False
        self.db = Db()
        self.max_score = self.db.read_score()
        self.asd = 0
        self.player_image = 'helis/ZF0.png'
        # self.user_id = 'Ryan'
        self.sign = Sign(self)
        self.restart()

    def process_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.VIDEORESIZE:
                self.screen_size = (event.w, event.h)
                surface = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                if self.state == 'sign':
                    self.screen.blit(pygame.transform.scale(self.background_sign_in, self.screen_size), (0, 0))
                else:
                    self.screen.blit(pygame.transform.scale(self.background_game, self.screen_size), (0, 0))
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = 'play'

    def game_logic(self):
        if self.a == 0:
            self.s += 50
        self.a += 1
        if self.a > self.s:
            random_y_1 = random.randint(0, self.screen_size[1])
            box1 = Box(self.screen_size[0], random_y_1, 1 + self.z, BLACK)
            self.box_group.add(box1)
            self.z += 0.1
            self.c = 0
            self.a = 0
            self.s -= 49

    def restart(self):
        self.save_done = False
        self.game_over = False
        self.score = 0
        self.c = 0
        self.z = 0
        self.s = 0
        self.a = 0
        self.score_c = 0
        self.s_accelerate = 0.1
        self.ccccc = 0
        self.player_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.player = Player(0, 0, self.player_image, self.screen)
        self.player_group.add(self.player)

    def display_frame(self):
        self.screen.blit(pygame.transform.scale(self.background_game, self.screen_size), (0, 0))
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(calc_score(self.score), True, BLACK)
        self.screen.blit(text, [0, 0])
        self.score_c += 1
        if self.score_c > 20:
            self.score += 1
            self.score_c = 0


            
        if not self.game_over:
            self.box_group.update()

            self.box_group.draw(self.screen)

            self.player_group.update()
            self.player_group.draw(self.screen)
            pos = pygame.mouse.get_pos()

            if pygame.sprite.spritecollide(self.player, self.box_group, False):
                self.game_over = True
                self.state = 'game_over'
  
        pygame.display.flip()

    def display_choose(self):
        self.screen.blit(pygame.transform.scale(self.background_game, self.screen_size), (0, 0))
        font = pygame.font.Font('wt014.ttf', 60)
        text = font.render("選擇玩家", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])

        images = ['helis/ZF0.png', 'helis/ZF1.png', 'helis/ZF2.png', 'helis/ZF3.png', 'helis/ZF4.png', 
        'helis/ZF5.png', 'helis/ZF6.png', 'helis/ZF7.png', 'helis/ZF8.png', 'helis/ZF9.png']
        hs = []

        for i in range(10):
            h0 = Heli(i * self.screen.get_width() / 10, self.screen.get_height() / 2, images[i])
            h = self.screen.blit(h0.image, h0.rect)
            hs.append([h, images[i]])




        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()

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

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if b.collidepoint(pos):
                    self.state = 'intro'
                    self.restart()
                    break

                for h in hs:
                    if h[0].collidepoint(pos):
                        self.player_image = h[1]
        pygame.display.flip()

    def display_game_over(self):
        self.screen.blit(pygame.transform.scale(self.background_game, self.screen_size), (0, 0))
        font = pygame.font.Font('wt014.ttf', 60)
        text = font.render("遊戲結束", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])
        
        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()

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
        if not self.save_done:
                if self.score > self.max_score:
                    self.db.save_score(self.score)
                    self.max_score = self.score
                    self.save_done = True

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if b.collidepoint(pos):
                    self.state = 'play'
                    self.restart()
                    break

        pygame.display.flip()

    def display_intro(self):
        self.screen.blit(pygame.transform.scale(self.background_game, self.screen_size), (0, 0))
        font = pygame.font.Font('wt014.ttf', 100)
        text = font.render("方塊戰爭", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 - 120
        self.screen.blit(text, [text_x, text_y])

        font3 = pygame.font.SysFont('Calibri', 30, True, False)
        text3 = font3.render(score_max(self.max_score), True, BLACK)
        self.screen.blit(text3, [0, 0])

        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()
        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 100
        start_btn = self.screen.blit(button, [button_x, button_y])
        
        font2 = pygame.font.Font('wt014.ttf', 30)
        text2 = font2.render("開始遊戲", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 100
        self.screen.blit(text2, [text2_x, text2_y])

        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()
        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 180
        choose_btn = self.screen.blit(button, [button_x, button_y])
        
        text2 = font2.render("選擇直升機", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 180
        self.screen.blit(text2, [text2_x, text2_y])

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if start_btn.collidepoint(pos):
                    self.state = 'play'
                    break
                if choose_btn.collidepoint(pos):
                    self.state = 'choose'
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
    g = Game(screen, screen_size)
    while True:
        g.process_events()

        if g.done: 
            break

        if g.state == 'signin':
            g.sign.display_sign_in()
        elif g.state == 'signup':
            g.sign.display_sign_up()
        elif g.state == 'intro':
            g.display_intro()
        elif g.state == 'choose':
            g.display_choose()
        elif g.state == 'game_over':
            g.display_game_over()
        elif g.state == 'play':
            g.game_logic()
            g.display_frame()

        clock.tick(60)

    pygame.quit()


main()