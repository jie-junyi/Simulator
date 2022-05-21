import pygame
from pygame.sprite import Sprite


class People(Sprite):
    """管理人的类"""

    def __init__(self, run_g):
        """初始化人"""
        super().__init__()
        self.screen = run_g.screen
        self.screen_rect = run_g.screen.get_rect()

        self.image = pygame.image.load('images/轮椅.png')
        self.image = pygame.transform.scale(self.image, (50, 60))

        self.rect = self.image.get_rect()

        self.x = float(50)
        self.y = float(50 + (self.screen_rect.height - 100) / 3 * 2 - self.rect.height)
        # 存储小数值。
        self.rect.x = self.x
        self.rect.y = self.y
        self.moving = float((self.screen_rect.height - 100) / 3)

        #  移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """人物移动"""
        if self.moving_up and (self.rect.y - (self.moving / 10 * 9)) > 0:
            self.y -= self.moving
        if self.moving_down and (self.rect.y + (self.moving / 10 * 9)) <= self.screen_rect.height:
            self.y += self.moving

        # 根据self.y更新rect对象。
        self.rect.y = self.y
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制人物。"""
        self.screen.blit(self.image, self.rect)
