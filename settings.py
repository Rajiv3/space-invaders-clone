class Settings:
    """class to store all the settings for the game"""
    def __init__(self):
        """Initlialize the settings"""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,230,230)
        self.ship_speed = 2.0
        self.ship_limit = 2
        # the bullets
        self.bullet_speed = 2.0   
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (100,0,0)
        self.bullets_max = 10
        # aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # moves to the right (-1 to the left)
