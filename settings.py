class Settings:
    """class to store all the settings for the game"""
    def __init__(self):
        """Initlialize the settings"""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,230,230)
        self.ship_limit = 2
        # the bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (100,0,0)
        self.bullets_max = 10
        # aliens
        self.fleet_drop_speed = 10

        # speed the game speeds up
        self.ship_speedup_scale = 1.1
        self.bullet_speedup_scale = 1.1
        self.alien_speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        these settings will change during the game
        Also used to reset the values on reset
        """
            
        self.ship_speed = 2.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1 # moves to the right (-1 to the left)
        
    def increase_speed(self):
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.bullet_speedup_scale
        self.alien_speed *= self.alien_speedup_scale
