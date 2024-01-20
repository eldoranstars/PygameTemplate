import sys
import pygame
import random
sys.path.append('rects')

from settings import Settings
from screen import Screen
from text import Text

settings = Settings()
screen = Screen(settings)
pause = Text(screen, "PAUSE: P or Start button", screen.rect.centerx, screen.rect.centery)
buttons = [pause]

# Получаем пиксельную маску для обработки коллизий.
def overlap(player, enemy):
    player.mask = pygame.mask.from_surface(player.surface)
    enemy.mask = pygame.mask.from_surface(enemy.surface)
    overlap = player.mask.overlap(enemy.mask, (enemy.rect.left - player.rect.left, enemy.rect.top - player.rect.top))
    return overlap

def collision(self, rect, wm, hm):
    # Получаем дополнительный прямоугольник для обработки коллизий.
    collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
    collision.center = rect.center
    return collision

# Вывод коллизий на экран.
def collision_test(object, wm, hm):
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

# Отслеживание нажатий клавиатуры и джойстика.
def check_events(stats, joystick_zero, joystick_one):
    if stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stats.game_active = False
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(7) == 1:
                    stats.game_active = False
    if not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_p:
                    stats.game_active = True
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(6) == 1:
                    pygame.quit()
                    sys.exit()
                if joystick.get_button(5) == 1:
                    if stats.music_active:
                        stats.music_active = False
                        pygame.mixer.pause()
                    else:
                        stats.music_active = True
                        pygame.mixer.unpause()
                if joystick.get_button(4) == 1:
                    pygame.display.toggle_fullscreen()
                if joystick.get_button(7) == 1:
                    stats.game_active = True

# pygame.key.get_pressed() используется для непрерывнной реакции на зажатую клавишу
def update_player(stats, joystick):
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == 1:
        pass
    if key[pygame.K_LEFT] == 1:
        pass
    if key[pygame.K_UP] == 1:
        pass
    if key[pygame.K_DOWN] == 1:
        pass
    if key[pygame.K_SPACE] == 1:
        pass
    if joystick:
        if joystick.get_axis(0) and joystick.get_axis(0) > 0.2:
            pass
        if joystick.get_axis(0) and joystick.get_axis(0) < -0.2:
            pass
        if joystick.get_axis(1) and joystick.get_axis(1) < -0.2:
            pass
        if joystick.get_axis(1) and joystick.get_axis(1) > 0.2:
            pass
        if joystick.get_axis(5) > 0.2:
            pass

# Вывод изображений на экран.
def blit_screen(stats):
    screen.blitme()
    if not stats.game_active:
        for button in buttons:
            button.blitme()
    pygame.display.update()