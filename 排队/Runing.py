import time

import pygame
import sys
from People import People
from Blocks import Block
import random
from Endline import Endline


class Running:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("排队之跑酷小游戏")
        # 设置背景色。
        self.bg_color = (0x63, 0x69, 0x86)
        self.image = pygame.image.load('images/组 42@2x.png')
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))

        self.image2 = pygame.image.load('images/矩形 4@3x.png')
        self.image2 = pygame.transform.scale(self.image2,
                                             (self.screen.get_width() - 100, (self.screen.get_height() - 100) / 3))
        self.image2.set_alpha(230)

        self.people = People(self)
        self.blocks_1 = pygame.sprite.Group()
        self.ends = pygame.sprite.Group()
        self.zz = 0
        self.z1 = 0
        self.z2 = 0
        self.z3 = 0
        # 自定义事件
        self.MYEVENT01 = pygame.USEREVENT + 1
        self.xx = int(random.randint(450, 800))
        pygame.time.set_timer(self.MYEVENT01, self.xx)

    def run(self):
        """开始跑酷事件"""
        while True:
            self._check_events()
            if self.zz == 50:
                time.sleep(1)
                self._create_line()
                self._create_line2()
                self.zz = 51
            self.people.update()
            self._update_blocks()
            self._update_screen()
            # 让最近绘制的屏幕可见。

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #  每次按键都被注册为一个KEYDOWN事件。
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # 判断事件触发情况
            elif event.type == self.MYEVENT01 and self.zz < 50:
                self._create_block()

    def _check_keydown_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_UP:
            self.people.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.people.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """响应松开。"""
        if event.key == pygame.K_UP:
            self.people.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.people.moving_down = False

    def _create_line(self):
        end = Endline(self, 0)
        end_width, end_height = end.rect.size
        end.x = self.screen.get_width()
        end.rect.x = end.x
        end.rect.y = 50
        self.ends.add(end)

    def _create_line2(self):
        for i in range(1, 4):
            end = Endline(self, 1)
            end_width, end_height = end.rect.size
            end.x = self.screen.get_width()
            end.rect.x = end.x
            if i == 1:
                end.rect.y = float(48 + (self.screen.get_rect().height - 100) / 3 - end_height)
            elif i == 2:
                end.rect.y = float(50 + (self.screen.get_rect().height - 100) / 3 * 2 - end_height)
            elif i == 3:
                end.rect.y = float(self.screen.get_rect().height - end_height - 50)
            self.ends.add(end)

    def _create_block(self):
        """创建一个障碍物"""
        block = Block(self)
        block_width, block_height = block.rect.size
        z = int(random.randint(1, 3))
        block.x = self.screen.get_width() - block_width
        block.rect.x = block.x
        if z == 1:
            self.z1 += 1
            if self.z1 < 4:
                block.rect.y = float(48 + (self.screen.get_rect().height - 100) / 3 - block_height)
            elif self.z2 < 4 and self.z2 < self.z3:
                self.z2 += 1
                self.z1 = 0
                block.rect.y = float(50 + (self.screen.get_rect().height - 100) / 3 * 2 - block_height)
            else:
                self.z3 += 1
                self.z1 = 0
                block.rect.y = float(self.screen.get_rect().height - block_height - 50)
        elif z == 2:
            self.z2 += 1
            if self.z2 < 4:
                block.rect.y = float(50 + (self.screen.get_rect().height - 100) / 3 * 2 - block_height)
            elif self.z1 < 4 and self.z1 < self.z3:
                self.z1 += 1
                self.z2 = 0
                block.rect.y = float(48 + (self.screen.get_rect().height - 100) / 3 - block_height)
            else:
                self.z3 += 1
                self.z2 = 0
                block.rect.y = float(self.screen.get_rect().height - block_height - 50)
        elif z == 3:
            self.z3 += 1
            if self.z3 < 4:
                block.rect.y = float(self.screen.get_rect().height - block_height - 50)
            elif self.z2 < 4 and self.z2 < self.z1:
                self.z2 += 1
                self.z3 = 0
                block.rect.y = float(50 + (self.screen.get_rect().height - 100) / 3 * 2 - block_height)
            else:
                self.z1 += 1
                self.z3 = 0
                block.rect.y = float(48 + (self.screen.get_rect().height - 100) / 3 - block_height)

        self.blocks_1.add(block)
        self.zz += 1

    def _people_hit(self):
        """人和障碍物碰撞的时候"""
        """!!!!!!!!!!"""

    def _update_blocks(self):
        """有障碍物到达边缘时采取相应的措施。"""
        self.blocks_1.update()
        self.ends.update()

        if pygame.sprite.spritecollideany(self.people, self.blocks_1):
            self._people_hit()

        if pygame.sprite.spritecollideany(self.people, self.ends):
            self._people_hit()

        for block in self.blocks_1.copy():
            if block.check_edges():
                self.blocks_1.remove(block)
                break

    def _draw_line(self):
        start_pos1 = 0, self.screen.get_rect().height / 3  # 起点
        end_pos1 = self.screen.get_rect().width, self.screen.get_rect().height / 3  # 终点

        start_pos2 = 0, self.screen.get_rect().height / 3 * 2  # 起点
        end_pos2 = self.screen.get_rect().width, self.screen.get_rect().height / 3 * 2  # 终点
        RED = (0x63, 0x69, 0x86)  # 定义红色
        pygame.draw.line(self.screen, RED, start_pos1, end_pos1, 1)  # 画线段
        pygame.draw.line(self.screen, RED, start_pos2, end_pos2, 1)  # 画线段

    def _draw_rect(self):
        self.screen.blit(self.image2, (50, 48))
        self.screen.blit(self.image2, (50, 50 + ((self.screen.get_height() - 100) / 3)))
        self.screen.blit(self.image2, (50, 50 + ((self.screen.get_height() - 100) / 3 * 2)))

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.image.get_rect())
        # 画三条赛道
        self._draw_line()
        self._draw_rect()
        self.people.blitme()
        self.blocks_1.draw(self.screen)
        if self.zz == 51:
            self.ends.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    r = Running()
    r.run()
