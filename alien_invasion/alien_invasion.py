import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import  Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import  Scoreboard



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

        #创建存储游戏统计信息的实例，并创建记分牌

        self.stats=GameStats(self)
        self.sb = Scoreboard(self) #注意前后顺序
        self.ship=Ship(self)

        #创建用于存储子弹的编组
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        #创建外星人
        self._create_fleet()

        #创建play按钮
        self.play_button=Button(self,'Play')

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

            if self.stats.game_active:
                self.ship.update()
                self._update_bulltes()
                self._update_aliens()
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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type==pygame.KEYDOWN:
             self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
               self._check_keyup_events(event)

    def _check_play_button(self,mouse_pose):
        """在玩家单击play按钮时开始新游戏,以及处理游戏结束的情况"""

        button_cliked=self.play_button.rect.collidepoint(mouse_pose)
        if button_cliked and not self.stats.game_active:


            #重置游戏设置
            self.settings.initialize_dynamic_settings()

            #隐藏光标
            pygame.mouse.set_visible(False)gi
            #处理游戏统计信息

            self.stats.reset_stats()
            self.stats.game_active=True

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            #创建一群新的外星人
            self._create_fleet()
            self.ship.center_ship()
    def _updae_screen(self):
        """ 更新屏幕上的图像，并切换到屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        self.aliens.draw(self.screen)

        #显示得分
        self.sb.show_score()
        self.sb.check_high_score()

        if not self.stats.game_active:
            self.play_button.draw_button()


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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        #删除发生碰撞的子弹和外星人
        collisions= collsions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():

                self.stats.score+=self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:

            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #提高等级
            self.stats.level+=1
            self.sb.prep_level()


    def _create_alien(self, alien_number,row_number):
        """创建一个外星人并将其放到前行"""
        alien = Alien(self)
        alien_with,alien_hight = alien.rect.size
        alien.x = alien_with + 2 * alien_with * alien_number
        alien.rect.x = alien.x
        alien.rect.y=alien_hight+2*alien_hight*row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """ 创建外星人 """
        #创建外星人
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        available_space_x =self.settings.screen_width-(2*alien_width)
        number_aliens_x=available_space_x//(2*alien_width)

        #计算屏幕可以容纳多少行外星人
        ship_hight=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_hight)
        number_rows=available_space_y//(2*alien_height)

        #创建第一行外星人
        for row_number in range(number_rows):
          for alien_number in range(number_aliens_x):
             self._create_alien(alien_number,row_number)
    def _update_aliens(self):
        """更新外星人位置,并在此之前检查是否有外星人在屏幕边缘"""
        self._check_fleet_edges()
        self.aliens.update()

        #检查外星人与飞船是否相碰
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #检查是否有外星人碰到底部
        self._check_aliens_bottom()

    #检测外星人是否碰到边缘
    def _check_fleet_edges(self):
        """外星人是否到达边缘，以及采取的行为"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """ 全部外星人下移动，并改变水平移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1



    def _ship_hit(self):
        """响应飞船被外星人撞到了"""
        if self.stats.ships_left>0:
        #将sheips_left减1,并更新
            self.stats.ships_left-=1
            self.sb.prep_ships()

            #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            #创建一群新的外星人，并将飞船放到屏幕底中央
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有外星人达到了屏幕底"""
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:
                #像外星人被撞到一样处理
                self._ship_hit()
                break




if  __name__ == '__main__':
    #创建游戏实例并运行游戏
    print("hello alien")
    ai=AilenInvasion()

    ai.run_game()