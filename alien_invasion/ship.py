import pygame

class Ship:

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩阵
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #对于每件新飞船，放在屏幕中央
        self.rect.midbottom=self.screen_rect.midbottom
        #self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """在指定位置绘画飞船"""
        self.screen.blit(self.image,self.rect)