import pygame
import sys
from settings import Settings

class Button:
    def __init__(self,ai_game,msg,x,y,i):
        """初始化按钮属性"""
        pygame.init()
        self.msg = msg
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        #设置按钮的尺寸和其它属性
        self.width, self.height = 200, 50
        #self.font_name = pygame.font.Font("font/my_font")
        self.button_color = (0xff,0xc7,0x61)
        self.text_color = (0,0,0)

        #创建按钮的rect对象
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self._prep_msg(msg,i)

    def _prep_msg(self,msg,i):
        self.font = pygame.font.Font("font/my_font.ttf",i)
        self.msg_image = self.font.render(msg,True,self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)







