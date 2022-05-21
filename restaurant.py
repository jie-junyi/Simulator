import pygame
import sys
from settings import Settings
from button import Button
from menu import Menu

class Restaurant:
    def __init__(self):
        """初始化基本信息"""
        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("食堂模拟器")

        # 设置开始按钮
        self.play_button_image = pygame.image.load('images/play.png')
        self.play_button_image_rect = self.play_button_image.get_rect()
        self.play_button_image_rect.centerx = self.screen_rect.width * 3 / 4 - 100
        self.play_button_image_rect.centery = self.screen_rect.height * 3 / 4 - 100
        # 设置问题图像
        self.question_image = pygame.image.load('images/question.PNG')
        self.question_image = pygame.transform.scale(self.question_image, (
            self.settings.screen_width / 2 - 100, self.settings.screen_height * 2 / 5 - 50))
        self.question_image_rect = self.question_image.get_rect()
        self.question_image_rect.centerx = self.play_button_image_rect.centerx
        self.question_image_rect.centery = self.screen_rect.centery - 200

        # 设置装饰画面
        self.decorate_image = pygame.image.load('images/decorate.PNG')
        self.decorate_image = pygame.transform.scale(self.decorate_image, (700, 500))
        self.decorate_image_rect = self.decorate_image.get_rect()
        self.decorate_image_rect.x = 20
        self.decorate_image_rect.centery = self.screen_rect.centery

        # 设置背景图片
        self.back_ground_image = pygame.image.load('images/rect.png')
        self.back_ground_image = pygame.transform.scale(self.back_ground_image,
                                                        (self.settings.screen_width, self.settings.screen_height))
        self.back_ground_image_rect = self.back_ground_image.get_rect()

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_buttondown(mouse_pos)

    def _check_mouse_buttondown(self,mouse_pos):
        if self.play_button_image_rect.collidepoint(mouse_pos):
            self.menu = Menu()
            self.menu.run_game()

    def _update_screen(self):
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.back_ground_image,self.back_ground_image_rect)
        self.screen.blit(self.play_button_image,self.play_button_image_rect)
        self.screen.blit(self.decorate_image,self.decorate_image_rect)
        self.screen.blit(self.question_image,self.question_image_rect)

if __name__ == '__main__':
    res = Restaurant()
    res.run_game()
