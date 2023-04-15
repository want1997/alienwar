import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


"""
首先创建一个空的pygame窗口，共之后用来绘制游戏元素，例如飞船和外星人。

"""


class AilenInvasion:
    """
    初始化游戏资源和行为的类
    """
    def __init__(self):
        pygame.init()

        #self.screen=pygame.display.set_mode((1200,800))  #利用Setting()来替代
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")  #设置窗口标题
        self.ship=Ship(self)

        #创建用于存储子弹的编组
        self.bullets=pygame.sprite.Group()

        #设置背景色(RGB,三元组红色，绿色，蓝色)
        #self.bg_color=(255,255,255)

    def run_game(self):
        """" 开始游戏的主循环"""
        while True:
            #监视键盘和鼠标事件
            """  
             for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            """

            """
            #每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)  #屏幕背景
            self.ship.blitme()                        #绘制飞船

            #让最近绘制的屏幕可见
            pygame.display.flip()
            """

            self._check_events()
            self.ship.update()
            self._update_bulltes()
            self._updae_screen()

            #消失的子弹

            """
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            
            """



    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
             self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
               self._check_keyup_events(event)


    def _updae_screen(self):
        """ 更新屏幕上的图像，并切换到屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        pygame.display.flip()

    def _check_keydown_events(self,event):
        """ 按键响应"""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            #按q退出
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        """创建一颗子弹，将其加入到编组bullets中 ，最大发射子弹有限制"""
        if len(self.bullets)< self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bulltes(self):

        """更新子弹位置并删除消失的子弹"""
        #更新位置
        self.bullets.update()
        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

if  __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai=AilenInvasion()

    ai.run_game()