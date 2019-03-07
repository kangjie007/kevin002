#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import sys

from ship6 import Ship
import game_function8 as gf
from pygame.sprite import Group

from settings import Settings

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('alien invasion4')

    ship=Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets=Group()


    while True:
        #gf.check_events()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.updata()
        gf.update_bullets(bullets)
        gf.updata_screen(ai_settings,screen,ship,bullets)


if __name__ == '__main__':
    run_game()