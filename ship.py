import pygame

# Pygame is efficient because it lets you treat all game elements like rectangles (rects), even if they're not exactly shaped like rectangles.
# Rectangles are simple geometric shapes; when Pygame needs to figure out whether two game elements have collided, for example, it can do this 
# more quickly if it treats each object as a rectangle.

class Ship:
    """ A class to manage the ship. """
    def __init__(self, ai_game):    # two parameters: self rerefence and current instance of alien invasion class.
        """ Initialize the ship and its starting position. """
        self.screen = ai_game.screen    # Screen is assigned as an attribute of ship.
        self.settings = ai_game.settings    # Settings attribute
        self.screen_rect = ai_game.screen.get_rect()    # Access and assign the screen's rect attribue

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')   # This function returns a surface representing the ship, and assigns it to self.image.
        self.rect = self.image.get_rect()   # When image loaded, get_rect() to access the ship's rect attribute to use later to place the ship.

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag: start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flags. """
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Keep the ship from moving off screen
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

# In Pygame, origin (0,0) is at top-left corner of screen, and coordinates increase as you go down and to the right.
# On a 1200x800 screen, bottom-right corner has coordinates (1200, 800). Note, this is the game window, not physical screen.

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)  # Note: blitme() method draws the image to the screen at the position specified by self.rect.