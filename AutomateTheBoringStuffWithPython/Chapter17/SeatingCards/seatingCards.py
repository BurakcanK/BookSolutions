""" Custom Seating Cards

Uses the `pillow` module to create images for custom seating cards for each of the guests listed
in `guests.txt`. Generates an image file with the guest name and some flowery decoration. Adds
equal black border to all of the images.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

# make the directory for invitation cards
os.makedirs('invitationCards', exist_ok=True)

# loop over the guests
with open('guests.txt', 'r') as guests:
    num = 1

    for guest in guests:
        # open image and add a border
        img = Image.open('flower.jpeg')
        img = ImageOps.expand(img, border=10, fill='black')

        # create a drawer object
        drawer = ImageDraw.Draw(img)

        # choose the fonts
        fontTitle = ImageFont.truetype(
            "/usr/share/fonts/opentype/malayalam/Manjari-Bold.otf", 50)
        fontDescription = ImageFont.truetype(
            "/usr/share/fonts/opentype/malayalam/Manjari-Regular.otf", 20)

        # write the text
        drawer.text((150, 200),
                    "It would be a pleasure to have the company of",
                    (187, 108, 187, 255),
                    fontDescription)

        drawer.text((200, 300),
                    guest,
                    (187, 108, 187, 255),
                    fontTitle)

        drawer.text((150, 450),
                    "at 11010 Memory Lane on the Evening of April 1st",
                    (187, 108, 187, 255),
                    fontDescription)

        # save the image and increment
        img.save('invitationCards/card' + str(num) + '.jpeg')
        num += 1
