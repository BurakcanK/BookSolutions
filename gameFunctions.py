import pygame
import sys


def checkEvents(ship):
    """ Respond the keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship to the right
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False


def updateScreen(aiSettings, screen, ship):
    # redraw the screen during each pass through the loop
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # make the most recently drawn screen visible
    pygame.display.flip()
