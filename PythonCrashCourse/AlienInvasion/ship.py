import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, aiSettings, screen):
        """ Initialize the ship and set its starting position. """
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        # movement flags
        self.movingRight = False
        self.movingLeft = False

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        """ Update the ship's position based on the movement flag. """
        # update the ship's center value, not the rect
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.aiSettings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeedFactor

        # update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)

    def centerShip(self):
        """ Center the ship on the screen. """
        self.center = self.screenRect.centerx
