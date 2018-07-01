import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in the fleet. """

    def __init__(self, aiSettings, screen):
        """ Initializes the alien and set its starting position. """
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the alien at its current location. """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Move the alien right or left. """
        self.x += (self.aiSettings.alienSpeedFactor *
                   self.aiSettings.fleetDirection)
        self.rect.x = self.x

    def checkEdges(self):
        """ Return True if alien is at edge of screen. """
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True
