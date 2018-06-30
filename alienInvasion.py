import pygame

import gameFunctions as gf
from settings import Settings
from ship import Ship


def run_game():
    # initialize game, settings and create a screen object
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))

    # make a ship
    ship = Ship(aiSettings, screen)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events, update the screen
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)

        # redraw the screen during each pass
        screen.fill(aiSettings.bgColor)


run_game()
