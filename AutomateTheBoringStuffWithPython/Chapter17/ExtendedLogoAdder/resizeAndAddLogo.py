""" Extending and Fixing the Chapter Project Programs - Adding a Logo

Resizes all the images in current working directory to fit in a 300x300 square, and adds catlogo.png
to the lower-right corner.
"""

import os
from PIL import Image

SQUARE_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# loop over all files in the working directory
for fileName in os.listdir('images'):
    fileName = fileName.lower()
    if not (fileName.endswith('.png') or
            fileName.endswith('.jpg') or
            fileName.endswith('.gif') or
            fileName.endswith('.bmp')) or fileName == LOGO_FILENAME:
        continue

    im = Image.open('images/' + fileName)
    width, height = im.size

    # resize the logo
    logoIm = logoIm.resize((width // 10, height // 10))
    logoWidth, logoHeight = logoIm.size

    # check if the image needs to be resized
    if width > SQUARE_SIZE and height > SQUARE_SIZE:
        # calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_SIZE / width) * height)
            width = SQUARE_SIZE
        else:
            width = int((SQUARE_SIZE / height) * width)
            height = SQUARE_SIZE

        # resize the image
        print("Resizing {}...".format(fileName))
        im = im.resize((width, height))

        # add the logo
        print("Adding logo to {}...".format(fileName))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # save changes
        im.save(os.path.join('withLogo', fileName))
