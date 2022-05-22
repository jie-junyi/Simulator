import pygame
import random


class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.bg_color = (0xff, 0xe9, 0xde)
        self.bg_color1 = (0x63, 0x69, 0x86)

        # 食堂信息
        self.restaurant1 = ['豆皮', '肠粉', '渔粉', '热干面',
                            '牛杂萝卜面', '过桥米线', '排骨汤', '蒸面点',
                            '小碗菜', '麻辣香锅', '汤粉', '水煮鱼',
                            '牛肉酱汁饭', '鸡柳饭', '烧肉饭', '土耳其烤肉饭',
                            '天津包子', '锡纸烧', '铁板饭', '黄焖鸡',
                            '小火锅', '匠心卤', '粥', '刀削面', '东北水饺']
        self.restaurant2 = ['水饺', '豆花', '生蚝鸡煲', '烧鹅饭',
                            '炒菜', '自选', '煲仔饭', '麻辣烫',
                            '水果捞', '炸鸡汉堡', '面点粥类', '粉面煎烙', '馄饨']
        self.restaurant3 = ['川菜', '湘西土钵菜', '煨烤联盟', '渔粉',
                            '粉面', '面点', '盖饭', '烤肉饭',
                            '米高林', '烤鸭饭', '小锅米线', '烧卤拌饭',
                            '港式扒饭', '自选菜', '小碗菜', '套餐',
                            '石锅菜', '辣子鸡', '烤盘饭', '小炒',
                            '炒饭', '鸡公煲', '舌尖大师铁板烧']
        self.restaurant4 = ['水煮鱼', '馄饨', '铁板饭', '面',
                            '水饺', '茶餐厅', '麻辣烫', '东苑菜馆']
        self.restaurant5 = ['基本套餐', '自选饭菜', '麻辣烫', '陕西面食',
                            '黄焖鸡', '小碗菜', '渔粉', '兰州拉面',
                            '面点粥类', '匠心卤', '焖锅', '土耳其烤肉饭',
                            '拌饭', '铁板饭', '意面', '麻辣香锅']

        # self.restaurants = {'restaurant1':'桂香园食堂','restaurant2':'东一食堂','restaurant3':'学子餐厅',
        #                     'restaurant4':'东二食堂','restaurant5':'南湖食堂'}
        self.restaurants1 = ['桂香园食堂', '东一食堂', '学子餐厅', '东二食堂', '南湖食堂']
        self.restaurants2 = [self.restaurant1, self.restaurant2, self.restaurant3, self.restaurant4, self.restaurant5]
