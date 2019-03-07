#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet
def check_keydown_events(event,ai_setting,screen,ship,bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)


def checn_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            checn_keyup_events(event,ship)

def fire_bullet(ai_setting,screen,ship,bullets):
    '''如果还没有到达限制，就发射一颗子弹'''
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)



def updata_screen(ai_setting,screen,ship,bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
def update_bullets(bullets):
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

if __name__ == '__main__':
    check_events()
    updata_screen()
