import pygame
from pygame.sprite import Group

import gameFunctions as gf
from button import Button
from gameStats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    # initialize game, settings and create a screen object
    pygame.init()
    aiSettings = Settings()
    # aiSettings.printAllSettings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))

    # make the Play button
    playButton = Button(aiSettings, screen, "Play")

    # create an instance to store game statistics
    stats = GameStats(aiSettings)

    # make a ship, a group of bullets and a group of aliens
    ship = Ship(aiSettings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.createFleet(aiSettings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events, update the screen
        gf.checkEvents(aiSettings, screen, stats,
                       playButton, ship, aliens, bullets)

        if stats.gameActive:
            ship.update()
            gf.updateBullets(aiSettings, screen, ship, aliens, bullets)
            gf.updateAliens(aiSettings, stats, screen, ship, aliens, bullets)

        gf.updateScreen(aiSettings, screen, stats, ship,
                        aliens, bullets, playButton)


run_game()
