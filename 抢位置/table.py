import pygame
from pygame.sprite import Sprite


class Table(Sprite):

    def __init__(self, grab_g):
        """初始化"""
        super().__init__()
        self.screen = grab_g.screen

        self.image = pygame.image.load('image/组 41@3x.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.rect.width + 50
        self.rect.y = self.rect.height + 50

        # 存储座位的精确水平位置。
        self.x = float(self.rect.x)
