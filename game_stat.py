class GameStats:
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Рекорд не должен сбрасываться.
        self.high_score = 0

        # Игра Aliens Invasion запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющеюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


