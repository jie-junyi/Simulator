from settings import Settings
import pygame
import sys
from button import Button
from 模拟器.y import sjb
import choose0
import restaurant

class choose:
    def __init__(self, msg_image):
        pygame.init()
        self.settings = Settings()
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()

        # 设置提示信息和边框
        self.suggest_message_image = pygame.image.load('images/rect1.png')
        self.suggest_message_image = pygame.transform.scale(self.suggest_message_image, (1200, 300))
        self.suggest_message_image_rect = self.suggest_message_image.get_rect()
        self.suggest_message_image_rect.centerx = self.screen_rect.centerx
        self.suggest_message_image_rect.centery = self.screen.get_height() / 3

        self.suggest_message = pygame.image.load(msg_image)
        self.suggest_message = pygame.transform.scale(self.suggest_message, (900, 150))
        self.suggest_message_rect = self.suggest_message.get_rect()
        self.suggest_message_rect.center = self.suggest_message_image_rect.center

        # 设置按钮
        self.return_button = Button(self, "返回首页", self.settings.screen_width / 4, self.settings.screen_height - 200, 40)
        self.return_button_rect = self.return_button.rect
        self.ok_button = Button(self, "开始闯关", self.settings.screen_width * 3 / 4, self.settings.screen_height - 200, 40)
        self.ok_button_rect = self.ok_button.rect

        # 设置背景图片
        self.back_ground = pygame.image.load('images/back_ground.png')
        self.back_ground = pygame.transform.scale(self.back_ground,
                                                  (self.settings.screen_width, self.settings.screen_height))
        self.back_ground_rect = self.back_ground.get_rect()

    def __run__(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_mouse(mouse_pos)

            self._update_screen()

    def _check_mouse(self, mouse_pos):
        if self.ok_button.rect.collidepoint(mouse_pos):
            sjb()
            ch = choose0.choose0('images/suggest.PNG')
            ch.__run__()
        elif self.return_button.rect.collidepoint(mouse_pos):
            res = restaurant.Restaurant()
            res.run_game()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color1)
        self.screen.blit(self.back_ground, self.back_ground_rect)
        self.screen.blit(self.suggest_message_image, self.suggest_message_image_rect)
        self.screen.blit(self.suggest_message, self.suggest_message_rect)
        self.return_button.draw_button()
        self.ok_button.draw_button()
        pygame.display.flip()



