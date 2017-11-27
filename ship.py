import pygame
import settings


class Ship():
    def __init__(self, screen, ship_state):
        '''初始化飞船并设置其初始位置'''

        self.screen = screen
        # self.ai_settings = ai_settings
        self.ship_state = ship_state

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的center属性中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def upLocationData(self):
        '''更新飞船位置数据'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ship_state.speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ship_state.speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ship_state.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ship_state.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
