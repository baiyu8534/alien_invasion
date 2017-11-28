class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_settings, ship_state, bullet_state, alien_state):
        self.alive = True
        self.ai_settings = ai_settings
        self.ship_state = ship_state
        self.bullet_state = bullet_state
        self.alien_state = alien_state
        self.reset_stats()

    def reset_stats(self):
        pass
