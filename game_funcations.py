import sys
import pygame

from bullet import Bullet


def check_events(ship, screen, bullets, bullet_state):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, bullets, bullet_state)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_keydown_events(event, ship, screen, bullets, bullet_state):
    if event.key == pygame.K_SPACE:
        file_bullet(bullet_state, bullets, screen, ship)
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_p:
        sys.exit()



def file_bullet(bullet_state, bullets, screen, ship):
    # 创建一颗子弹，并加入到编组中
    if (len(bullets) < bullet_state.allowed):
        new_bullet = Bullet(bullet_state, screen, ship)
        bullets.add(new_bullet)


def updata_screen(ai_setting, screen, ship, bullets):
    '''更新屏幕上的图像并且换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.drow_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

