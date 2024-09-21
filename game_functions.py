import sys
import pygame
import random
sys.path.append('rects')

from settings import Settings
from screen import Screen
from text import Text

settings = Settings()
screen = Screen(settings)
game_start = Text(screen, "START", screen.rect.centerx, screen.rect.centery)
game_settings = Text(screen, "SETTINGS", screen.rect.centerx, screen.rect.centery + 33)
game_board = Text(screen, "LEADERBOARD", screen.rect.centerx, screen.rect.centery + 66)
game_quit = Text(screen, "EXIT", screen.rect.centerx, screen.rect.centery + 99)
buttons = [game_start, game_settings, game_board, game_quit]

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
    if stats.game_screen == "main_menu":
        print(pygame.key.get_pressed())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    buttons[0], buttons[1], buttons[2], buttons[3] = buttons[3], buttons[0], buttons[1], buttons[2]
                    buttons[0].text_color = (200, 0, 0)
                    buttons[0].rect.bottom = screen.rect.centery
                    buttons[1].rect.bottom = screen.rect.centery + 33
                    buttons[2].rect.bottom = screen.rect.centery + 66
                    buttons[3].rect.bottom = screen.rect.centery + 99
                if event.key == pygame.K_DOWN:
                    buttons[0], buttons[1], buttons[2], buttons[3] = buttons[1], buttons[2], buttons[3], buttons[0]
                    buttons[0].text_color = (200, 0, 0)
                    buttons[0].rect.bottom = screen.rect.centery
                    buttons[1].rect.bottom = screen.rect.centery + 33
                    buttons[2].rect.bottom = screen.rect.centery + 66
                    buttons[3].rect.bottom = screen.rect.centery + 99
                if event.key == pygame.K_SPACE:
                    if buttons[0].msg == "START":
                        stats.game_screen = "game_start"
                    if buttons[0].msg == "SETTINGS":
                        stats.game_screen = "game_settings"
                    if buttons[0].msg == "LEADERBOARD":
                        stats.game_screen = "game_board"
                    if buttons[0].msg == "EXIT":
                        pygame.quit()
                        sys.exit()
    if not stats.game_screen == "main_menu":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stats.game_screen = "main_menu"

    # if not stats.game_active:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.key == pygame.K_m:
    #                 if stats.music_active:
    #                     stats.music_active = False
    #                     pygame.mixer.pause()
    #                 else:
    #                     stats.music_active = True
    #                     pygame.mixer.unpause()
    #             if event.key == pygame.K_f:
    #                 pygame.display.toggle_fullscreen()
    #             if event.key == pygame.K_p:
    #                 stats.game_active = True
    #                 if stats.final_active:
    #                     new_game(stats)
            # if event.type == pygame.JOYBUTTONDOWN:
            #     if joystick.get_button(6) == 1:
            #         pygame.quit()
            #         sys.exit()
            #     if joystick.get_button(5) == 1:
            #         if stats.music_active:
            #             stats.music_active = False
            #             pygame.mixer.pause()
            #         else:
            #             stats.music_active = True
            #             pygame.mixer.unpause()
            #     if joystick.get_button(4) == 1:
            #         pygame.display.toggle_fullscreen()
            #     if joystick.get_button(7) == 1:
            #         stats.game_active = True

# запуск новой игры
def new_game(stats):
    settings.new_game()
    stats.final_active = False

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

# Обновить расположение объектов на экране.
def update_final_text():
    for message in settings.final_text:
        message.scroll_text()

# Создание объектов в списке
def append_messages():
    for message in settings.messages:
        settings.first_line += 33
        new_message = Text(screen, message, screen.rect.centerx, screen.rect.bottom + settings.first_line)
        settings.final_text.append(new_message)
    settings.messages.clear()

# Вывод изображений на экран.
def blit_screen(stats):
    screen.blitme()
    if not stats.final_active and not stats.game_active:
        for button in buttons:
            button.blitme()
    if stats.final_active:
        for message in settings.final_text:
            message.blitme()
        if not stats.game_active:
            gf.update_final_text()
            gf.append_messages()
    pygame.display.update()