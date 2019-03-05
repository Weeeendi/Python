import sys

import pygame
from settings import Settings
from ship import Ship
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Creating a ship
    ship = Ship(screen)
    

    #设置背景色
    #bg_color = (230, 230, 230)
    

    #开始游戏的主循环
    while True:
        #overlook the active of mouse or keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
			elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #向右移动飞船
				    ship.rect.centerx += 1

			     
				    
        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()