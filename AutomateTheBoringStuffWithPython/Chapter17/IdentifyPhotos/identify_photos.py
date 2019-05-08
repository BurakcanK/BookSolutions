"""Identify Photo Folders on the Hard Drive

Go through every folder on your hard drive and find potential photo folders, which is any
folder where more than half of the files are photos.
"""

import os
from PIL import Image

PATH_TO_ROOT = r"<path_to_root>"

for folder_name, sub_folders, filenames in os.walk(PATH_TO_ROOT):
    num_photo_files = 0
    num_non_photo_files = 0

    for filename in filenames:
        # check if file extension isn't .png or .jpg
        if not filename.endswith('.jpg'):
            num_non_photo_files += 1
            continue

        try:
            # open image file using Pillow
            img = Image.open(os.path.abspath(
                os.path.join(folder_name, filename)))

            # check if width & height are larger than 500
            if img.width > 500 or img.height > 500:
                # image is large enough to be a photo
                num_photo_files += 1
            else:
                # image is too small to be a photo
                num_non_photo_files += 1
        except OSError as e:
            print(">> Image", filename, "can not be opened.\nError:", e)

    # if more than half of files were photos
    # print the absolute path of the folder
    if num_photo_files > num_non_photo_files:
        print(os.path.abspath(folder_name))
