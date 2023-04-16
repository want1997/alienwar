class Settings:
    """ 存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255,255,255)

        #飞船设置
        self.ship_speed=0.5
        self.ship_limit=3

        #外星人设置,外星人撞到边缘后，向下移动，水平方向变换移动
        self.alien_speed=0.1
        self.fleet_drop_speed=50
        #fleet_direction 为1为右，-1为左
        self.fleet_direction=1



        #子弹设置
        self.bullet_speed =1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)


        #限制子弹最大数量
        self.bullets_allowed=3
