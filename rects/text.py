import pygame
pygame.font.init()

class Text():
    def __init__(self, screen, msg, posx, posy, text_color = (200, 200, 200), score = 0):
        # Атрибуты класса
        self.screen = screen
        self.msg = msg
        self.font = pygame.font.SysFont(None, 33)
        # Загрузка изображения и получение прямоугольника
        self.update_text(text_color)
        self.rect = self.surface.get_rect()
        # Получение начальных координат изображения
        self.rect.centerx = posx
        self.rect.bottom = posy

    def update_text(self, text_color = (200, 200, 200), score = 0):
        self.score_msg = self.msg.format(score)
        self.surface = self.font.render(self.score_msg, True, text_color)

    def scroll_text(self):
        self.rect.centery -= 1

    # Вывод изображения на экран
    def blitme(self):
        self.screen.surface.blit(self.surface, self.rect)