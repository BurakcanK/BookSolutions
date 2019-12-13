"""Image Site Downloader

Go to a photo-sharing website Flickr and search for
a category of photos, download the resulting images.
"""

import os
import re
import requests
from bs4 import BeautifulSoup

SCRIPT_DIR = os.path.dirname(__file__)

photo_counter = 0

print("Accessing flickr..")
response = requests.get("https://www.flickr.com/search/?text=cute")
soup = BeautifulSoup(response.text, "html.parser")

print("Parsing flickr..")
# links are in style tags which are in divs
for div in soup.find_all("div", class_="photo-list-photo-view"):
    style = div.get("style")
    if not style:
        continue

    # extract the url from the style
    match = re.search(r"(?<=url\().*?(?=(_\w)?.jpg\))", style)
    if match:
        # arrange the url according to Flickr standards and download
        photo_url = match.group() + "_b.jpg"
        photo = requests.get("http:" + photo_url)

        # if response is an unavailable image continue
        if photo.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable_l.png" or\
           photo.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable.png":
            continue
        # check for status errors
        photo.raise_for_status()

        # arrange photo file name
        photo_path = os.path.join(
            SCRIPT_DIR,
            "photos/photo{:03}.jpg".format(photo_counter)
        )

        # write the .jpg to the file
        with open(photo_path, "wb") as photo_file:
            print("Writing to the file", )

            for chunk in photo.iter_content(100000):
                photo_file.write(chunk)

            photo_counter += 1
