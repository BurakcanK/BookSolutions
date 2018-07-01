import pygame
from pygame.sprite import Group

import gameFunctions as gf
from settings import Settings
from ship import Ship


def run_game():
    # initialize game, settings and create a screen object
    pygame.init()
    aiSettings = Settings()
    # aiSettings.printAllSettings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))

    # make a ship, a group of bullets and a group of aliens
    ship = Ship(aiSettings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.createFleet(aiSettings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events, update the screen
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateAliens(aiSettings, aliens)
        gf.updateScreen(aiSettings, screen, ship, aliens, bullets)


run_game()
