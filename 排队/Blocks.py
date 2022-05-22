import pygame
from pygame.sprite import Sprite
import random


class Block(Sprite):
    """障碍物"""

    def __init__(self, run_g):
        """初始化"""

        super().__init__()
        self.screen = run_g.screen
        self.screen_rect = run_g.screen.get_rect()

        block = {1: 'imagee/多人-人群@2x.png', 2: 'imagee/多人-人群@3x.png', 3: 'imagee/大型障碍物@3x.png', 4: 'imagee/摩托车@3x.png'}

        filename = block[random.randint(1, 4)]
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (50, 60))

        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right - self.rect.width - 50
        self.rect.y = self.rect.height

        # 存储障碍物的精确水平位置。
        self.x = float(self.rect.x)

        self.zz = int(random.randint(5, 10))

    def check_edges(self):
        """如果障碍物位于屏幕边缘，就返回True。"""
        if self.rect.left <= 25:
            return True

    def update(self):
        """往左移动10格"""
        self.x -= 15
        self.rect.x = self.x
