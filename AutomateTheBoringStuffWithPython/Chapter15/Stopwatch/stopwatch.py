"""Prettified Stopwatch

Expanded version of the project Stopwatch from Chapter 15. This version uses "rjust", "ljust"
string methods to "prettify" the output.
"""

import time

# displays the program's instructions
print("Press ENTER to begin. Afterwards, press Enter to 'click' the stopwatch.\n"
      "Press CTRL-C to quit.")

# press Enter to begin
input()
print("Started")
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        print("Lap #{:3}: {:6.2f} ({:6.2f})".format(
            lap_num, total_time, lap_time), end="")
        lap_num += 1

        # reset the last lap time
        last_time = time.time()

except KeyboardInterrupt:
    # handle the CTRL-C exception to keep its error message from displaying
    print("\nDone")
