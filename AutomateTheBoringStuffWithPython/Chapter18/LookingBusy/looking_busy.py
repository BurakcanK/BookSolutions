"""Looking Busy

Nudge the mouse cursor slightly every 10 seconds.
"""

import pyautogui
import time

while True:
    # move the mouse a pixel and back
    pyautogui.moveRel(0, 1)
    pyautogui.moveRel(0, -1)

    # wait
    time.sleep(10)
