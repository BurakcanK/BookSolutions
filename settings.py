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

        # bullet settings
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3

        # alien settings
        self.alienSpeedFactor = 1
        self.fleetDropSpeed = 10
        # fleetDirection of 1 represents right; -1 represents left
        self.fleetDirection = 1

    def printAllSettings(self):
        print("Screen width:", self.screenWidth)
        print("Screen height:", self.screenHeight)
        print("Background color:", self.bgColor)
        print("Ship speed:", self.shipSpeedFactor)
        print("Bullet speed:", self.bulletSpeedFactor)
        print("Bullet width:", self.bulletWidth)
        print("Bullet height:", self.bulletHeight)
        print("Bullet color:", self.bulletColor)
