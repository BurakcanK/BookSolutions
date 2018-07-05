import pygame
import sys
from time import sleep

from bullet import Bullet
from alien import Alien


def checkKeyDownEvents(event, aiSettings, screen, ship, bullets):
    """ Respond to key presses. """
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def checkKeyUpEvents(event, ship):
    """ Respond to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False


def checkEvents(aiSettings, screen, stats, playButton, ship, aliens, bullets):
    """ Respond the keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(aiSettings, screen, stats,
                            playButton, ship, aliens, bullets, mouseX, mouseY)


def updateScreen(aiSettings, screen, stats, ship, aliens, bullets, playButton):
    # redraw the screen during each pass through the loop
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()

    # draw the aliens
    aliens.draw(screen)

    # draw the play button if the game is inactive
    if not stats.gameActive:
        playButton.drawButton()

    # make the most recently drawn screen visible
    pygame.display.flip()


def updateBullets(aiSettings, screen, ship, aliens, bullets):
    """ Update position of bullets and get rid of old bullets. """
    # update bullet positions
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    checkBulletAlienCollisions(aiSettings, screen, ship, aliens, bullets)

    if len(aliens) == 0:
        # destroy existing bullets and create new fleet
        bullets.empty()
        createFleet(aiSettings, screen, ship, aliens)


def checkBulletAlienCollisions(aiSettings, screen, ship, aliens, bullets):
    """ Respond to bullet-alien collisions. """
    # remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)


def fireBullet(aiSettings, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet. """
    # create a new bullet and add it to the bullets group
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)


def getNumberAliensX(aiSettings, alienWidth):
    """ Determine the number of aliens that fit in a row. """
    availableSpaceX = aiSettings.screenWidth - 2 * alienWidth
    numberAliensX = int(availableSpaceX / (2 * alienWidth))
    return numberAliensX


def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
    """ Create an alien and place it in the row. """
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)


def createFleet(aiSettings, screen, ship, aliens):
    """ Create a full fleet of aliens. """
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width
    alien = Alien(aiSettings, screen)
    numberAliensX = getNumberAliensX(aiSettings, alien.rect.width)
    numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)

    # create the fleet of aliens
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)


def getNumberRows(aiSettings, shipHeight, alienHeight):
    """ Determine the number of rows of aliens that fit on the screen. """
    availableSpaceY = (aiSettings.screenHeight -
                       (3 * alienHeight) - shipHeight)
    numberRows = int(availableSpaceY / (2 * alienHeight))
    return numberRows


def updateAliens(aiSettings, stats, screen, ship, aliens, bullets):
    """ Check if the fleet is at an edge, and then update the
    positions of all aliens in the fleet. """
    checkFleetEdges(aiSettings, aliens)
    aliens.update()

    # look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(aiSettings, stats, screen, ship, aliens, bullets)

    # look for aliens hitting the bottom of the screen
    checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets)


def checkFleetEdges(aiSettings, aliens):
    """ Respond appropriately if any aliens have reached an edge. """
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break


def changeFleetDirection(aiSettings, aliens):
    """ Drop the entire fleet and change the fleet's direction. """
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1


def shipHit(aiSettings, stats, screen, ship, aliens, bullets):
    """ Respond to ship being hit by alien. """
    if stats.shipsLeft > 0:
        # decrement ships left
        stats.shipsLeft -= 1

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        createFleet(aiSettings, screen, ship, aliens)
        ship.centerShip()

        # pause
        sleep(0.5)
    else:
        stats.gameActive = False
        pygame.mouse.set_visible(True)


def checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets):
    """ Check if any aliens have reached the bottom of the screen. """
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            # treat this the same as if the ship got hit
            shipHit(aiSettings, stats, screen, ship, aliens, bullets)
            break


def checkPlayButton(aiSettings, screen, stats, playButton, ship, aliens, bullets, mouseX, mouseY):
    """ Start a new game when the player clicks Play. """
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not stats.gameActive:
        # hide the mouse cursor
        pygame.mouse.set_visible(False)

        # reset the game statistics
        stats.resetStats()
        stats.gameActive = True

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        createFleet(aiSettings, screen, ship, aliens)
        ship.centerShip()
