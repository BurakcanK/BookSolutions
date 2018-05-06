""" Prettified Stopwatch

Expanded version of the project Stopwatch from Chapter 15. This version uses 'rjust', 'ljust'
string methods to 'prettify' the output.
"""

import time

# displays the program's instructions
print("Press ENTER to begin. Afterwards, press Enter to 'click' the stopwatch.\n\
Press CTRL-C to quit.")

# press Enter to begin
input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        print("Lap #{:3}: {:6.2f} ({:6.2f})".format(
            lapNum, totalTime, lapTime), end='')
        lapNum += 1

        # reset the last lap time
        lastTime = time.time()

except KeyboardInterrupt:
    # handle the CTRL-C exception to keep its error message from displaying
    print("\nDone")
