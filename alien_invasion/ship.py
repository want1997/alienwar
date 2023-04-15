import pygame

class Ship:

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings = ai_game.settings


        #加载飞船图像并获取其外接矩阵
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()



        #对于每件新飞船，放在屏幕中央
        self.rect.midbottom=self.screen_rect.midbottom
        #self.rect.midtop = self.screen_rect.midtop

        #在飞船的属性中存储小数数值
        self.x=float(self.rect.x)
        #移动标志
        self.moving_right=False
        self.moving_left=False

    def blitme(self):
        """在指定位置绘画飞船"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        """根据移动标志调整飞船的位置,并限制其出界"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed

        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        self.rect.x=self.x


