import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''管理飞船发射的子弹的类'''

    def __init__(self, bullet_state, screen, ship):
        '''在飞船所处位置创建一个子弹'''
        # super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen

        # 在0,0处创建一个子弹的矩形，在设置正确位置
        self.rect = pygame.Rect(0,0,bullet_state.width,bullet_state.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = bullet_state.color
        self.speed = bullet_state.speed

    def update(self):
        '''子弹向上移动'''
        self.y -= self.speed

        self.rect.y = self.y

    def drow_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)