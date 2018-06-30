class Settings():
    """ A class to store all the settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's settings. """
        # screen settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)

        # ship settings
        self.shipSpeedFactor = 1.5
