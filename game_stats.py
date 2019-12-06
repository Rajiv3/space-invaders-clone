class GameStats:
    """stats tracking"""

    def __init__(self, ai_game):
        """initialize the stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """initialize the stats that can change mid-game"""
        self.ships_left = self.settings.ship_limit
