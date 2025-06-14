# Alien Invasion Game Phase 1

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ Initiliaze the game, and create game resources. """
        pygame.init()
        self.clock = pygame.time.Clock()    # Defines the pygame clock for Frame Rate control.
        self.settings = Settings()  # Instance of Settings.

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # Attributes taken from self.settings
        pygame.display.set_caption("Alien Invasion")
            # OPTION FOR FULLSCREEN SETTINGS: replace above self.screen attribute with:
            # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            # self.settings.screen_width = self.screen.get_rect().width
            # self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)  # Create an instance of Ship after the screen has been created.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60) # Loop will run 60 times per second.
    
    def _check_events(self): # _ lead indicates a helper class.
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():    # Event loop to listen for events. This function returns a list of events that have taken place since the last time the function was called.
            if event.type == pygame.QUIT:   # When player clicks game window's close button.
                sys.exit()  # Game exit
            elif event.type == pygame.KEYDOWN:      # KEYDOWN in pygames = key pressed.
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:    # KEYUP in pygames = key is released (no longer pressed down).
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to key presses. """
        if event.key == pygame.K_RIGHT:     # K_RIGHT = right arrow key.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:    # K_LEFT = left arrow key.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:   # End game if player presses Q.
            sys.exit()
        elif event.key == pygame.K_SPACE:   # K_SPACE = space key
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        if len(self.bullets) < self.settings.bullets_allowed:   # Enforces bullets_allowed setting.
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    # add() method is similar to append(), but specifically for Pygame groups.

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():  # Copy() method needed since you can't remove items from a list/group within a for loop; so we loop over a copy.
            if bullet.rect.bottom <= 0:     # Remove bullets that have reached the top of the screen.
                self.bullets.remove(bullet)
        # Use this line to test if # bullets is decreasing: print(len(self.bullets))

    def _create_fleet(self):
        """ Create the fleet of faliens. """
        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)

    def  _update_screen(self):           
        """ Update images on the screen, and flip to the new screen """
        self.screen.fill(self.settings.bg_color)    # Use self.settings to access the BG color when filling the screen.
        for bullet in self.bullets.sprites():   # Loop to draw the list of bullets to the screen
            bullet.draw_bullet()
        self.ship.blitme()  # We draw the ship on the screen so it appears on top of the background.
        self.aliens.draw(self.screen)   # And we draw the alien fleet.
        # Make the most recently drawn screen visible.
        pygame.display.flip()   # Continually updates the while loop, erasing the old screen so only the new is visible.

if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

