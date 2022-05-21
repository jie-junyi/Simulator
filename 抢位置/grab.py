import time

import pygame
import sys
from table import Table
from table2 import Table2
import pygame.font
import random


class Grab:
    def __init__(self):
        """初始化"""

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('抢位置')

        self.tables = pygame.sprite.Group()
        self.z = 0
        self.zz = 0
        self.font = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont('SimHei', 48)
        self.time = 3
        # 设置背景色。
        self.bg_color = (0x63, 0x69, 0x86)
        self.image = pygame.image.load('image/组 42@2x.png')
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))
        self.image2 = pygame.image.load('image/矩形 5@3x.png')
        self.image2 = pygame.transform.scale(self.image2,
                                             (self.screen.get_width() - 100, self.screen.get_height() - 100))

        # 自定义事件
        self.MYEVENT01 = pygame.USEREVENT + 1
        self.MYEVENT02 = pygame.USEREVENT + 2
        pygame.time.set_timer(self.MYEVENT01, 100)
        pygame.time.set_timer(self.MYEVENT02, 4000)
        self._create_tables()
        self._chang_table()
        self.prep_time()
        self.prep_paper()
        self.prep_shu()

    def run(self):
        """开始抢占事件"""
        while True:
            self._check_events()
            if self.time == 0:
                if self.z < 20:
                    time.sleep(1)
                elif self.z >= 20:
                    break
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #  每次按键都被注册为一个MOUSEBUTTONDOWN事件。
            elif event.type == pygame.MOUSEBUTTONDOWN and self.time >= 0.1:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse(mouse_pos)
            # 判断定时器
            elif event.type == self.MYEVENT01 and self.time >= 0.1:
                self.time -= 0.1
                self.prep_time()
            elif event.type == self.MYEVENT02 and self.time == 0:
                self.tables.empty()
                self._create_tables()
                self._chang_table()
                self.time = 3
                self.z = 0

    def _check_keydown_events(self, event):
        """响应按键。"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def prep_time(self):
        """将倒计时转换为渲染的图像。"""
        self.time = round(self.time, 1)
        time_str = str(self.time)

        self.time_image = self.font.render(time_str, True,
                                           self.bg_color, (0xFF, 0xFF, 0xFF))
        # 将时间放在屏幕下面
        self.time_rect = self.time_image.get_rect()
        self.time_rect.y = 70
        self.time_rect.x = self.screen.get_width() - 70 - self.time_rect.width

    def prep_paper(self):
        """将倒计时转换为渲染的图像。"""

        paper_str = "快找到空位置"

        self.paper_image = self.font2.render(paper_str, True,
                                             self.bg_color, (0xFF, 0xFF, 0xFF))
        # 将时间放在屏幕下面
        self.paper_rect = self.paper_image.get_rect()
        self.paper_rect.y = self.image2.get_rect().y + self.paper_rect.height + 30
        self.paper_rect.x = self.image2.get_rect().x + self.paper_rect.width / 2 - 50

    def prep_shu(self):
        """将点击次数转换为渲染的图像。"""

        shu_str = str(self.z)

        self.shu_image = self.font.render(shu_str, True,
                                          self.bg_color, (0xFF, 0xFF, 0xFF))
        # 将时间放在屏幕下面
        self.shu_rect = self.shu_image.get_rect()
        self.shu_rect.y = 70
        self.shu_rect.x = self.screen.get_width() / 2

    def _draw_rect(self):
        self.screen.blit(self.image2, (50, 48))

    def _check_mouse(self, mouse_pos):
        """点击事件"""
        tb = self.tables.sprites()[-1]
        button_clicked = tb.rect.collidepoint(mouse_pos)
        if button_clicked:
            self.z += 1
            self.prep_shu()

    def _chang_table(self):
        self.zz = int(random.randint(0, 27))
        tb = self.tables.sprites()[self.zz]
        table = Table2(self)
        table.rect = tb.rect
        self.tables.remove(tb)
        self.tables.add(table)

    def _create_table(self, num, row_num):
        """创建桌子"""
        table = Table(self)
        table_width, table_height = table.rect.size
        table.x = table_width + 2 * table_width * num + 50
        table.rect.x = table.x
        table.y = table.rect.height + 1.3 * table.rect.height * row_num + 130
        table.rect.y = table.y
        self.tables.add(table)

    def _create_tables(self):

        table = Table(self)
        table_width, table_height = table.rect.size

        available_space_x = self.screen.get_width() - (2 * table_width) + 100
        number_table_x = available_space_x // (2 * table_width)

        # 计算屏幕可容纳多少行桌子。
        available_space_y = (self.screen.get_height() - table_height + 50)
        number_rows = available_space_y // (2 * table_height)
        # 创建外星人群。
        for row_number in range(number_rows):
            for table_number in range(number_table_x):
                self._create_table(table_number, row_number)

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.image.get_rect())
        self._draw_rect()
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.paper_image, self.paper_rect)
        self.screen.blit(self.shu_image, self.shu_rect)
        self.tables.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    r = Grab()
    r.run()
