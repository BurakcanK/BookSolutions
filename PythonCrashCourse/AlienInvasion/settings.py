class Settings():
    """ A class to store all the settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's static settings. """
        # screen settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)

        # ship settings
        self.shipLimit = 3

        # bullet settings
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3

        # alien settings
        self.fleetDropSpeed = 10

        # how quickly the game and score speeds up
        self.speedUpScale = 1.2
        self.scoreScale = 1.5

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        """ Initialize settings that change throughout the game. """
        self.shipSpeedFactor = 1.5
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 1

        # fleet direction, 1 for right, -1 for left
        self.fleetDirection = 1

        # scoring
        self.alienPoints = 50

    def increaseSpeed(self):
        """ Increase speed settings and alien point values. """
        self.shipSpeedFactor *= self.speedUpScale
        self.bulletSpeedFactor *= self.speedUpScale
        self.alienSpeedFactor *= self.speedUpScale

        self.alienPoints *= self.scoreScale

    def printAllSettings(self):
        print("Screen width:", self.screenWidth)
        print("Screen height:", self.screenHeight)
        print("Background color:", self.bgColor)
        print("Ship speed:", self.shipSpeedFactor)
        print("Bullet speed:", self.bulletSpeedFactor)
        print("Bullet width:", self.bulletWidth)
        print("Bullet height:", self.bulletHeight)
        print("Bullet color:", self.bulletColor)
