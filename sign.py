import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Sign:
    def __init__(self, game):
        self.g = game
        self.screen = self.g.screen
        self.input_id = ''
        self.input_pwd = ''
        self.input_idpwd = 'id'

    def display_sign_in(self):
        self.screen.blit(pygame.transform.scale(self.g.background_sign_in, self.g.screen_size), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    if self.input_idpwd == 'id':
                        self.input_id = self.input_id[:-1]    
                    else:
                        self.input_pwd = self.input_pwd[:-1]
                else:
                    if self.input_idpwd == 'id':
                        if len(self.input_id) < 8:
                            self.input_id += event.unicode
                    else:
                        if len(self.input_pwd) < 8:
                            self.input_pwd += event.unicode
  
                
        font = pygame.font.Font('wt014.ttf', 30)

        # 帳號密碼
        text = font.render("帳號:", True, BLACK) 
        text_rect = text.get_rect()
        id_x = self.screen.get_width() / 2 - text_rect.width / 2 - 100
        id_y = self.screen.get_height() / 2 - text_rect.height / 2 - 100
        self.screen.blit(text, [id_x, id_y])
        
        text_input_id = font.render(self.input_id, True, (0,0,0))
        self.screen.blit(text_input_id, (id_x + 100,id_y))

        id_block = pygame.draw.rect(self.screen, BLACK, [id_x + 90, id_y - 5, 250, 40], 1)

        text = font.render("密碼:", True, BLACK) 
        text_rect = text.get_rect()
        pwd_x = self.screen.get_width() / 2 - text_rect.width / 2 - 100
        pwd_y = self.screen.get_height() / 2 - text_rect.height / 2 - 0
        self.screen.blit(text, [pwd_x, pwd_y])
        
        text_input_pwd = font.render(self.input_pwd, True, (0,0,0))
        self.screen.blit(text_input_pwd, (pwd_x + 100, pwd_y))
        pwd_block = pygame.draw.rect(self.screen, BLACK, [pwd_x + 90, pwd_y - 5, 250, 40], 1)


        # 按鈕
        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()
        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 100
        signin_btn = self.screen.blit(button, [button_x, button_y])

        text = font.render("登入", True, BLACK) 
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2 + 100
        self.screen.blit(text, [text_x, text_y])
        
      
        button = pygame.Surface((200, 70))
        button.fill(RED)
        button_rect = button.get_rect()
        button_x = self.screen.get_width() / 2 - button_rect.width / 2
        button_y = self.screen.get_height() / 2 - button_rect.height / 2 + 180
        signup_btn = self.screen.blit(button, [button_x, button_y])

        text2 = font.render("註冊", True, BLACK)
        text2_rect = text2.get_rect()
        text2_x = self.screen.get_width() / 2 - text2_rect.width / 2
        text2_y = self.screen.get_height() / 2 - text2_rect.height / 2 + 180
        self.screen.blit(text2, [text2_x, text2_y])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if signup_btn.collidepoint(pos):
                    self.state = 'signup'
                    break

                if signin_btn.collidepoint(pos):
                    print('sign in')
                    # asdasdasdasasd
                    break

                if id_block.collidepoint(pos):
                    print('wtf')
                    self.input_idpwd = 'id'
                if pwd_block.collidepoint(pos):
                    print('wtfx2')
                    self.input_idpwd = 'pwd'


        pygame.display.flip()


    def display_sign_up(self):
        pass