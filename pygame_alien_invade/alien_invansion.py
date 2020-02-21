import sys
import pygame
import game_function as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import  Button
from scoreboard import Scoreboard


def run_game():
    """ 初始化游戏并创建一个屏幕对象 """
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invansion")

    # 创建play按钮
    play_button = Button(ai_settings,screen,"Play")

    # 创建一个用与存储游戏同喜统计信息的实例 并设置记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    #创建一艘飞船 、创建一个用于存储子弹的编组、创建一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group() 
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    """ 开始游戏的主循环 """
    while True:
        gf.check_event(ai_settings, screen, stats,sb,play_button,ship, aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            
        gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button)


run_game()

