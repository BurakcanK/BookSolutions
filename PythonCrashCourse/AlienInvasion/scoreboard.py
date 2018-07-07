import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """ A class to report scoring information. """

    def __init__(self, aiSettings, screen, stats):
        """ Initialize scorekeeping attributes. """
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats

        # font settings for scoring information
        self.textColor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepShips()

    def prepScore(self):
        """ Turn the score into a rendered image. """
        roundedScore = int(round(self.stats.score, -1))
        scoreStr = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render(
            scoreStr, True, self.textColor, self.aiSettings.bgColor)

        # display the score at the top right of the screen
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepHighScore(self):
        """ Turn the high score into a rendered image. """
        highScore = int(round(self.stats.highScore, -1))
        highScoreStr = "{:,}".format(highScore)
        self.highScoreImage = self.font.render(
            highScoreStr, True, self.textColor, self.aiSettings.bgColor)

        # center the high score at the top of the screen
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top

    def showScore(self):
        """ Draw scores and ships to the screen. """
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)

        # draw the ships
        self.ships.draw(self.screen)

    def prepLevel(self):
        """ Turn the level into a rendered image. """
        self.levelImage = self.font.render(
            str(self.stats.level), True, self.textColor, self.aiSettings.bgColor)

        # position the level below the score
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def prepShips(self):
        """ Show how many ships are left. """
        self.ships = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = Ship(self.aiSettings, self.screen)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
