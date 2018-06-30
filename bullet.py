import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """

    def __init__(self, aiSettings, screen, ship):
        """ Create a bullet object at the ship's current position. """
        super().__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, aiSettings.bulletWidth, aiSettings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor

    def update(self):
        """ Move the bullet up the screen. """
        # update the decimal position of the bullet
        self.y -= self.speedFactor
        # update the rect position
        self.rect.y = self.y

    def drawBullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
