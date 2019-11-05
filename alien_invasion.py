import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """overall class, used to manage assests/behaviours"""

    def __init__(self):
        """initialize the game, create the game resources"""
        # initialize background settings
        pygame.init()
        self.settings = Settings()
        
        # to run in fullscreen, delete next line and uncomment following
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Aliens")
        self.bg_colour = (230, 230, 230)
        self.ship = Ship(self)

    def run_game(self):
        """starts main loop for game"""
        while True: 
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _update_screen(self):
        """updates images on screen"""
        # redraw screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # makes the most recently drawn screen visible
        pygame.display.flip()
    
    def _check_events(self):
        # event loop watches for KBM events. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """function to respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:        
            self.ship.moving_left = True
        # quit the game
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """function to respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:        
            self.ship.moving_left = False


if __name__ == '__main__':
    # make the game instance and run it
    ai = AlienInvasion()
    ai.run_game()
