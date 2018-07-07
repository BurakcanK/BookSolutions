class GameStats():
    """ Track the statistics for Alien Invasion. """

    def __init__(self, aiSettings):
        """ Initialize statistics. """
        self.aiSettings = aiSettings
        self.resetStats()

        # start game in an inactive state
        self.gameActive = False

        # high score should never be reset
        self.highScore = 0

    def resetStats(self):
        """ Initialize statistics that can change during the game. """
        self.shipsLeft = self.aiSettings.shipLimit
        self.score = 0
        self.level = 1
