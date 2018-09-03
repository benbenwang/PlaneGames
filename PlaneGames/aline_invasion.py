import pygame
from pygame.sprite import Group

import main_package.game_functions as game_functions
from main_package.button import Button
from main_package.scoreboard import Scoreboard
from main_package.ship import Ship
from tools.game_states import GameState
from tools.settings import Settings


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人群
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameState(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_bullets(ai_settings, screen, aliens, stats, sb, ship, bullets)
            game_functions.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets, stats, sb, play_button)


run_game()
