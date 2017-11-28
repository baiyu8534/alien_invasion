import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''外星人'''

    def __init__(self, screen,alien_state):
        super().__init__()
        self.screen = screen
        self.alien_state = alien_state

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width / 2
        self.rect.y = self.rect.height / 2

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def biltme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        self.x += (self.alien_state.speed_x * self.alien_state.fleet_direction)
        self.rect.x = self.x

    def check_is_edges(self):
        '''检查外星人是否移动的边缘'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
