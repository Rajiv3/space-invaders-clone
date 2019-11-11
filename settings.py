class Settings:
    """class to store all the settings for the game"""
    def __init__(self):
        """Initlialize the settings"""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        # the bullets
        self.bullet_speed = 1.0    
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (100,0,0)
        self.bullets_max = 10
