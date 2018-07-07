import pygame.font


class Button():

    def __init__(self, aiSettings, screen, msg):
        """ Initialize button attributes. """
        self.screen = screen
        self.screenRect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.buttonColor = (50, 155, 50)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        # the button message needs to be prepped only once
        self.prepMsg(msg)

    def prepMsg(self, msg):
        """ Turn msg into a rendered image and center text on the button. """
        self.msgImage = self.font.render(
            msg, True, self.textColor, self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        """ Draw blank button and then draw message. """
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)
