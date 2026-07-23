# значения game_screen могуть быть:
# [ main_menu, game_start, game_settings, leaderboard ]

class GameStats():
    def __init__(self):
        self.game_screen = "main_menu"
        self.game_active = False
        self.final_active = False
        self.music_active = True