class BulletState():
    '''子弹的状态'''
    def __init__(self):
        self.power = 1
        self.speed = 1
        self.width = 3
        self.height = 15
        self.color = 60, 60, 60
        # 最大子弹数量
        self.allowed = 5

