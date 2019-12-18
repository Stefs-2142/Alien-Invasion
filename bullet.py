import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенным кораблём"""

    def __init__(self, ai_setting, screen, ship):
        """Создаёт объекту пули в текущей позиции корабля."""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пуои сохраняется в вещественном формате.
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """ Перемещщает пулю вверх по экрану."""

        # Обновление позиции пули в вещественном формате.
        self.y -= self.speed_factor

        # Обеовление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """ Вывод пули на экран."""

        pygame.draw.rect(self.screen, self.color, self.rect)
