import sys
import pygame
from settings import Settings
from ship import Ship
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

        #设置背景色(RGB,三元组红色，绿色，蓝色)
        #self.bg_color=(255,255,255)

    def run_game(self):
        """" 开始游戏的主循环"""
        while True:
            #监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            #每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)  #屏幕背景
            self.ship.blitme()                        #绘制飞船

            #让最近绘制的屏幕可见
            pygame.display.flip()





if  __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai=AilenInvasion()
    ai.run_game()