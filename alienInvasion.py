import pygame
from pygame.sprite import Group

import gameFunctions as gf
from settings import Settings
from ship import Ship


def run_game():
    # initialize game, settings and create a screen object
    pygame.init()
    aiSettings = Settings()
    aiSettings.printAllSettings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))

    # make a ship
    ship = Ship(aiSettings, screen)
    # make a group to store the bullets in
    bullets = Group()

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events, update the screen
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(aiSettings, screen, ship, bullets)


run_game()
