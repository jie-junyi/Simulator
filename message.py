import pygame
from settings import Settings

class Message:
    def __init__(self,ai_game,msg,color,x,y,i):
        """初始化信息属性"""
        pygame.init()
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        #设置信息属性
        self.font = pygame.font.Font("font/my_font.ttf",i)
        self.msg_image = self.font.render(msg, True, color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = x
        self.msg_image_rect.centery = y

    def draw_message(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)