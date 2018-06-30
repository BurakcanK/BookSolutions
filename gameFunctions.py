import pygame
import sys

from bullet import Bullet


def checkKeyDownEvents(event, aiSettings, screen, ship, bullets):
    """ Respond to key presses. """
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)


def checkKeyUpEvents(event, ship):
    """ Respond to key releases. """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False


def checkEvents(aiSettings, screen, ship, bullets):
    """ Respond the keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)


def updateScreen(aiSettings, screen, ship, bullets):
    # redraw the screen during each pass through the loop
    screen.fill(aiSettings.bgColor)
    ship.blitme()

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()

    # make the most recently drawn screen visible
    pygame.display.flip()


def updateBullets(bullets):
    """ Update position of bullets and get rid of old bullets. """
    # update bullet positions
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fireBullet(aiSettings, screen, ship, bullets):
    """ Fire a bullet if limit not reached yet. """
    # create a new bullet and add it to the bullets group
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
