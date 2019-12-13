"""Extending and Fixing the Chapter Project Programs - Adding a Logo

Resize all the images in current working directory to fit in a 300x300 square, and add catlogo.png
to the lower-right corner.
"""

import os
from PIL import Image

SQUARE_SIZE = 300
LOGO_FILENAME = "catlogo.png"

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs("with-logo", exist_ok=True)
# loop over all files in the working directory
for filename in os.listdir("images"):
    filename = filename.lower()
    if not (filename.endswith(".png") or
            filename.endswith(".jpg") or
            filename.endswith(".gif") or
            filename.endswith(".bmp")) or filename == LOGO_FILENAME:
        continue

    im = Image.open("images/" + filename)
    width, height = im.size

    # resize the logo
    logo_im = logo_im.resize((width // 10, height // 10))
    logo_width, logo_height = logo_im.size

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
        print("Resizing {}...".format(filename))
        im = im.resize((width, height))

        # add the logo
        print("Adding logo to {}...".format(filename))
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

        # save changes
        im.save(os.path.join("with-logo", filename))
