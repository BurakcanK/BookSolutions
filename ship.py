import pygame


class Ship():
    def __init__(self, screen):
        """ Initialize the ship and set its starting position. """
        self.screen = screen

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

    def update(self):
        """ Update the ship's position based on the movement flag. """
        if self.movingRight:
            self.rect.centerx += 1
        if self.movingLeft:
            self.rect.centerx -= 1

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
