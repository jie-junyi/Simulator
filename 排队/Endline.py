import pygame
from pygame.sprite import Sprite


class Endline(Sprite):
    def __init__(self, run_g, c):
        """初始化"""
        super().__init__()
        self.screen = run_g.screen
        self.screen_rect = run_g.screen.get_rect()
        self.image1 = pygame.image.load('images/直线 3@3x.png')
        self.image1 = pygame.transform.scale(self.image1, (5, (self.screen.get_height() - 100)))

        self.image2 = pygame.image.load('images/胜利@3x.png')
        self.image2 = pygame.transform.scale(self.image2, (50, 60))

        if c == 0:
            self.image = self.image1
            self.rect = self.image1.get_rect()
        elif c == 1:
            self.image=self.image2
            self.rect = self.image2.get_rect()

        self.rect.x = self.screen_rect.right - self.rect.width - 50
        self.rect.y = self.rect.height
        # 存储障碍物的精确水平位置。
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果障碍物位于屏幕边缘，就返回True。"""
        if self.rect.left <= 25:
            return True

    def update(self):
        """往左移动10格"""
        self.x -= 15
        self.rect.x = self.x
