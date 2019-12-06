import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.stats = GameStats(self)

        pygame.display.set_caption("Aliens")
        self.bg_colour = (230, 230, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """starts main loop for game"""
        while True: 
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
        
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
        elif event.key == pygame.K_SPACE:        
            self._fire_bullet()
        # quit the game
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """function to respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:        
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet object, add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """updates images on screen"""
        # redraw screen each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # makes the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        """remove the bullets once they are off the screen"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # check for any bullets that have hit aliens
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()        

    def _ship_hit(self):
        """respond to the destruciton of the ship"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        """updates positions of the aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _create_fleet(self):
        """create the aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """create alien"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_aliens_bottom(self):
        """check if any aliens have reach the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # can do the same thing as a ship collision
                self._ship_hit
                break

    def _check_fleet_edges(self):
        """flip direction if aliens reach the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    # make the game instance and run it
    ai = AlienInvasion()
    ai.run_game()
