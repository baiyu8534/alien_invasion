class AlienState():

    def __init__(self):
        # 1.5倍外星人宽度
        self.interval_x = 1.5

        # 1.5倍外星人高度
        self.interval_y = 1.5

        self.speed_x = 1
        self.speed_y = 3

        # 舰队方向 1右移 -1 左移
        self.fleet_direction = 1
