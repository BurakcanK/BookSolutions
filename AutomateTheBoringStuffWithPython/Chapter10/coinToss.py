""" Debugging Coin Toss

This program has several bugs in it, therefore by using 'logging' and 'debugging'
we are going to find the bugs that keep the program from working correctly.
"""

import random

import logging
logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.DEBUG)

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug("guess: %s", guess)

# 0 is tails, 1 is heads
toss = random.randint(0, 1)
logging.debug("toss (wrong): %s", toss)

# solution for this problem
toss = ('heads', 'tails')[toss]
logging.debug("toss (correct): %s", toss)

if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guesss = input()
    if toss == guesss:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
