""" Identify Photo Folders on the Hard Drive

Goes through every folder on your hard drive and finds potential photo folders, which is any
folder where more than half of the files are photos.
"""

PATH_TO_ROOT = r"<pathToRoot"

import os
from PIL import Image

for folderName, subFolders, fileNames in os.walk(PATH_TO_ROOT):
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    for fileName in fileNames:
        # check if file extension isn't .png or .jpg
        if not fileName.endswith('.jpg'):
            numNonPhotoFiles += 1
            continue

        try:
            # open image file using Pillow
            img = Image.open(os.path.abspath(
                os.path.join(folderName, fileName)))

            # check if width & height are larger than 500
            if img.width > 500 or img.height > 500:
                # image is large enough to be a photo
                numPhotoFiles += 1
            else:
                # image is too small to be a photo
                numNonPhotoFiles += 1
        except OSError as e:
            print(">> Image", fileName, "can not be opened.\nError:", e)

    # if more than half of files were photos
    # print the absolute path of the folder
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(folderName))
