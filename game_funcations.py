import sys
import pygame

from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_F1:
        bullet_state.speed += 1
    elif event.key == pygame.K_F2:
        if bullet_state.speed > 1:
            bullet_state.speed -= 1
    elif event.key == pygame.K_F3:
        bullet_state.allowed += 1
    elif event.key == pygame.K_F4:
        if bullet_state.allowed > 5:
            bullet_state.allowed -= 1


def file_bullet(bullet_state, bullets, screen, ship):
    # 创建一颗子弹，并加入到编组中
    if len(bullets) < bullet_state.allowed:
        new_bullet = Bullet(bullet_state, screen, ship)
        bullets.add(new_bullet)


def updata_screen(ai_setting, screen, ship, bullets, aliens):
    '''更新屏幕上的图像并且换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.drow_bullet()

    ship.blitme()
    # 会绘制编组中每个元素
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets, aliens):
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中敌人
    # 击中后子弹和敌人都消失
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_aliens(aliens, alien_state):
    check_fleet_edges(aliens, alien_state)
    aliens.update()


def create_fleet(ai_setting, screen, alien_state, aliens, ship_height):
    alien_width = get_alien_width(screen, alien_state)
    alien_height = get_alien_height(screen, alien_state)
    number_alien_x = get_number_alien_x(ai_setting, alien_width, alien_state)
    rows_number = get_number_rows(ai_setting, alien_height, ship_height, alien_state)
    for row_number in range(rows_number):
        for alien_number in range(number_alien_x):
            alien = create_alien(screen, alien_state, alien_width, alien_height, alien_number, row_number)
            aliens.add(alien)


def get_alien_width(screen, alien_state):
    alien = Alien(screen, alien_state)
    return alien.rect.width


def get_alien_height(screen, alien_state):
    alien = Alien(screen, alien_state)
    return alien.rect.height


def check_fleet_edges(aliens, alien_state):
    for alien in aliens.sprites():
        if alien.check_is_edges():
            change_fleet_direction(aliens, alien_state)
            break


def change_fleet_direction(aliens, alien_state):
    for alien in aliens.sprites():
        # alien.y += alien_state.speed_y
        alien.rect.y += alien_state.speed_y
    alien_state.fleet_direction *= -1


def get_number_alien_x(ai_setting, alien_width, alien_state):
    available_space_x = ai_setting.screen_width - alien_width
    return int(available_space_x / (alien_state.interval_x * alien_width))


def create_alien(screen, alien_state, alien_width, alien_height, alien_number, rows_number):
    alien = Alien(screen, alien_state)
    alien.x = alien_width / 2 + alien_state.interval_x * alien_width * alien_number
    alien.y = alien_height / 2 + alien_state.interval_y * alien_height * rows_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    return alien


def get_number_rows(ai_setting, alien_height, ship_height, alien_state):
    available_space_y = ai_setting.screen_height - 2 * alien_height - ship_height
    return int(available_space_y / (alien_state.interval_y * alien_height))
