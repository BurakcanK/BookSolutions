"""2048

Go to the "https://gabrielecirulli.github.io/2048/" and play the game
automatically by sending random "up-down-right-left" keystrokes to the website.

You need to have "chromedriver" installed for selenium to work.
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open up Chrome and go to the game
driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")
time.sleep(2)

# select the whole page and define keys
elem = driver.find_elements_by_tag_name("html")
keys = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

print("Starting to play the game..")
for i in range(100):
    # send a random key from keys
    elem[0].send_keys(keys[random.randint(0, 3)])
    time.sleep(1)
print("\nStopped playing.")