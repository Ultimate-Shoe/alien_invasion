
class Settings:
    """ A class to store all settings for Alien Invasion. """
    
    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 1200    # Display size in pixels
        self.screen_height = 800
        self.bg_color = (230, 230, 230)     # Set the background color.

        # Ship settings
        self.ship_speed = 1.5   # Ship moves 1.5 pixels per loop

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5