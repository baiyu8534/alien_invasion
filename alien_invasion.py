import sys
import pygame
from settings import Settings
from ship import Ship
from ship_state import ShipState
from bullet_state import BulletState
import game_funcations as gf
from pygame.sprite import Group


def run_game():
    ''' 初始化游戏并创建一个屏幕'''
    pygame.init()
    ai_settings = Settings()
    ship_state = ShipState()
    bullet_state = BulletState()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(screen, ship_state)
    # 创建一个存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监视加键盘鼠标
        gf.check_events(ship, screen, bullets, bullet_state)
        ship.upLocationData()

        gf.update_bullets(bullets)

        # 更新屏幕显示
        gf.updata_screen(ai_settings, screen, ship, bullets)


run_game()
