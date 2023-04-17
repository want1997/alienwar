class Settings:
    """ 存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255,255,255)

        #飞船设置
        #self.ship_speed=0.5
        self.ship_limit=2

        #外星人设置,外星人撞到边缘后，向下移动，水平方向变换移动
        #self.alien_speed=0.1
        self.fleet_drop_speed=20
        #fleet_direction 为1为右，-1为左
        self.fleet_direction=1



        #子弹设置
        #self.bullet_speed =1.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)


        #限制子弹最大数量
        self.bullets_allowed=3

        #加快游戏节奏的速度
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()

        #外星人分数提高
        self.score_scale=1.5



    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=0.2

        #击落一个外星人得分
        self.alien_points=50

        # fleet_direction 为1为右，-1为左
        self.fleet_direction = 1
    def increase_speed(self):
        """提高速度设置,外星人分数"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_points=int(self.alien_points*self.score_scale)
        #print(self.alien_points)





