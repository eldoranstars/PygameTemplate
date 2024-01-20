import pygame
import game_functions as gf
import stats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Pygame Template")
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
stats = stats.GameStats()

while True:
    clock.tick(60)
    joystick_zero = pygame.joystick.Joystick(0) if pygame.joystick.get_count() else ''
    joystick_one = pygame.joystick.Joystick(1) if pygame.joystick.get_count() else ''
    gf.check_events(stats, joystick_zero, joystick_one)
    gf.blit_screen(stats)