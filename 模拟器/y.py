import time
from pickletools import read_unicodestring1
from turtle import screensize  # 导入随机模块
import random  # 导入随机模块
import pygame
import sys


def sjb():
    flag = 1
    # 初始化
    pygame.init()
    # 设置主屏幕
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # 填充游戏
    screen.fill((255, 255, 255))
    # 设置游戏名称
    pygame.display.set_caption('和阿姨决斗')
    # 引入字体类型（先省略）
    # 矩形区域(颜色填充的是线)
    pygame.draw.rect(screen, (0, 0, 0), [30, 80, 400, 300], 2)
    # 分割线
    pygame.draw.line(screen, (0, 0, 0), [30, 230], (430, 230), 2)
    # 圆
    # 当width设置为0或者不设置时,画出来的是实心的圆
    pygame.draw.circle(screen, (0, 0, 0), [230, 175], 20, width=1)
    pygame.draw.circle(screen, (0, 0, 0), [97, 325], 20, width=1)
    pygame.draw.circle(screen, (0, 0, 0), [230, 325], 20, width=1)
    pygame.draw.circle(screen, (0, 0, 0), [357, 325], 20, width=1)
    # #矩形区域(颜色填充的是区域)
    # pygame.draw.rect(screen,(255,255,255),(30,80,400,300),2)

    # 写字
    f = pygame.font.Font('字魂24号.ttf', 25)
    f2 = pygame.font.Font('字魂24号.ttf', 40)
    text = f.render("Aunt(auto)", True, (0, 0, 0), (255, 255, 255))
    text2 = f.render("Player", True, (0, 0, 0), (255, 255, 255))
    textwin = f2.render("you win your aunt!!!", True, (255, 0, 0), (255, 255, 255))
    textlose = f2.render("you lose to your aunt...", True, (255, 0, 0), (255, 255, 255))

    # 获得显示对象的 rect区域大小
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRectwin = textwin.get_rect()
    textRectlose = textlose.get_rect()
    # 设置显示对象居中
    textRect.center = (230, 110)
    textRect2.center = (230, 265)
    textRectwin.center = (650, 380)
    textRectlose.center = (650, 380)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    # screen.blit(textwin,textRectwin)
    # screen.blit(textlose,textRectlose)

    # 加载游戏说明的图片
    # 不能直接复制路径，这里的路径斜杠方向向右
    image_surface = pygame.image.load("图片/游戏说明.png").convert()
    image_surfacep1 = pygame.image.load("图片/形式政策.png")
    image_surfacep2 = pygame.image.load("图片/圆规.png")
    image_surfacep3 = pygame.image.load("图片/剪刀.png")
    image_surfacea1 = pygame.image.load("图片/锅铲.jpg")
    image_surfacea2 = pygame.image.load("图片/饭勺.jpg")
    image_surfacea3 = pygame.image.load("图片/夹子.jpg")
    # 缩放图片
    image_p1 = pygame.transform.scale(image_surfacep1, (30, 30))
    image_p2 = pygame.transform.scale(image_surfacep2, (30, 30))
    image_p3 = pygame.transform.scale(image_surfacep3, (30, 30))
    image_a1 = pygame.transform.scale(image_surfacea1, (30, 30))
    image_a2 = pygame.transform.scale(image_surfacea2, (30, 30))
    image_a3 = pygame.transform.scale(image_surfacea3, (30, 30))

    # 叉号退出固定代码段
    # 如果无此主循环代码，运行结果一闪而过

    num = 0
    yin_num = 0
    shu_num = 0
    # f = 0

    while flag:
        for event in pygame.event.get():
            # 判断用户是否点了"x",并执行if代码段
            if event.type == pygame.QUIT:
                # 卸载所有模块
                pygame.quit()
                # 终止程序，确保退出程序
                sys.exit()
            screen.blit(image_surface, (480, 150))
            screen.blit(image_p1, (82, 310))
            screen.blit(image_p2, (215, 310))
            screen.blit(image_p3, (342, 310))
            pygame.display.update()
            if yin_num == 2:
                screen.blit(textwin, textRectwin)
                pygame.display.update()
                time.sleep(2)
                flag = 0
                continue
            if shu_num == 2:
                screen.blit(textlose, textRectlose)
                pygame.display.update()
                time.sleep(2)
                flag = 0
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                # x,y=pygame.mouse.get_pos() #获取坐标
                x, y = event.pos
                if (77 < x < 117) and (305 < y < 345):
                    m = 0
                elif (210 < x < 250) and (305 < y < 345):
                    m = 1
                elif (337 < x < 377) and (305 < y < 345):
                    m = 2
                else:
                    continue

                com = random.randint(0, 2)
                if com == 0:
                    screen.blit(image_a1, (215, 160))
                    pygame.display.update()
                if com == 1:
                    screen.blit(image_a2, (215, 160))
                    pygame.display.update()
                if com == 2:
                    screen.blit(image_a3, (215, 160))
                    pygame.display.update()

                if (m == 0 and com == 0) or (m == 1 and com == 1) or (m == 2 and com == 2):
                    print('你赢了')
                    yin_num += 1
                    num += 1
                else:
                    print('你输了')
                    shu_num += 1
                    num += 1
                t = 'win-%d:lose-%d' % (yin_num, shu_num)
                text3 = f.render(t, True, (0, 0, 0), (255, 255, 255))
                textRect3 = text3.get_rect()
                textRect3.center = (580, 110)
                screen.blit(text3, textRect3)



