import pygame
import sys


def checkKeyDownEvents(event, ship):
    """ Respond to key presses. """
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True


def checkKeyUpEvents(event, ship):
    """ Respond to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False


def checkEvents(ship):
    """ Respond the keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, ship)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)


def updateScreen(aiSettings, screen, ship):
    # redraw the screen during each pass through the loop
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # make the most recently drawn screen visible
    pygame.display.flip()
