class Settings:
    """Класс для хранения всех настроек игры Alien Invaison."""

    def __init__(self):
        """"Инициализирует настройки игры """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметры пулии
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        # Настройки корабля
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Настройка пришельца
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 -влево.
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speed_scale = 1.1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющие в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Подсчёт очков
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо, а -1 -влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """ Увеличивает настро+йки скорости и стоимости пришельцев"""
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
