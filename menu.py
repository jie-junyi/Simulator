import pygame
from settings import Settings
import sys
from settings import Settings
from button import Button
from message import Message
import random
from 排队.Runing import Running
from 排队.People import People


class Menu:
    def __init__(self):
        """初始化菜单信息"""
        pygame.init()
        self.bg_color = (0xFF, 0xFF, 0xFF)
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()

        # 更换按钮
        self.change_button = pygame.image.load('images/change.png')
        self.change_button_rect = self.change_button.get_rect()
        self.change_button_rect.centerx = 400
        self.change_button_rect.y = 500
        # 确认按钮
        self.ok_button = pygame.image.load('images/ok.png')
        self.ok_button_rect = self.ok_button.get_rect()
        self.ok_button_rect.centerx = 1000
        self.ok_button_rect.y = 500

    def run_game(self):
        self._update_screen()
        self._blit_screen()
        while True:
            self._check_events()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_buttondown(mouse_pos)

    def _check_mouse_buttondown(self, mouse_pos):
        if self.change_button_rect.collidepoint(mouse_pos):
            self._update_screen()
            self._blit_screen()
        elif self.ok_button_rect.collidepoint(mouse_pos):
            self.run = Running()
            self.run.run()

    def _blit_screen(self):
        # 设置背景图片
        self.back_ground_image = pygame.image.load('images/rect.png')
        self.back_ground_image = pygame.transform.scale(self.back_ground_image,
                                                        (self.settings.screen_width, self.settings.screen_height))
        self.back_ground_image_rect = self.back_ground_image.get_rect()
        # 绘制背景和按钮
        self.screen.blit(self.back_ground_image, self.back_ground_image_rect)
        self.screen.blit(self.change_button, self.change_button_rect)
        self.screen.blit(self.ok_button, self.ok_button_rect)

    def _update_screen(self):
        # 渲染信息
        self.screen.fill(self.bg_color)
        i = random.randint(0, 4)
        restaurant = self.settings.restaurants1[i]
        restaurant1 = self.settings.restaurants2[i]
        food = random.choice(restaurant1)

        text_color = (255, 255, 255)
        self.restaurant_message = Message(self, f"为你生成的食堂是:{restaurant}", text_color, self.screen_rect.centerx, 250, 40)
        self.food_message = Message(self, f"为你生成的菜品是:{food}", text_color, self.screen_rect.centerx, 350, 40)

        # 随机取出食堂和食堂中的食物
        self.restaurant_message.draw_message()
        self.food_message.draw_message()
        pygame.display.flip()
