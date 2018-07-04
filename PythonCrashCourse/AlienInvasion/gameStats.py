class GameStats():
    """ Track the statistics for Alien Invasion. """

    def __init__(self, aiSettings):
        """ Initialize statistics. """
        self.aiSettings = aiSettings
        self.resetStats()

        # start Alien Invasion in an active state
        self.gameActive = True

    def resetStats(self):
        """ Initialize statistics that can change during the game. """
        self.shipsLeft = self.aiSettings.shipLimit
