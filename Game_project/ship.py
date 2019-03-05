import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船"""
        self.screen = screen
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r'C://Users//Administrator//Desktop//python_work//Game_project//image//ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将飞船放置在屏幕底下的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """在指定位置放置飞船"""
        self.screen.blit(self.image,self.rect)