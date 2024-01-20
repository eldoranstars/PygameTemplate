import pygame
import sys
import os

# Get absolute path to resource, works for dev and for PyInstaller
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Settings():
    def __init__(self):
        pygame.init()
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen_color = (100, 100, 100)
        self.midline_width = self.screen_height / 100
        self.midline_height = self.screen_height
        # Параметры изображений
        # self.road_surface = pygame.image.load(resource_path('media/road.jpg'))
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED)
        # self.midline_surface = pygame.Surface((self.midline_width, self.midline_height))
        # Параметры аудио
        # self.intro_sound = pygame.mixer.Sound(resource_path('media/intro.mp3'))
        # self.outro_sound = pygame.mixer.Sound(resource_path('media/outro.mp3'))