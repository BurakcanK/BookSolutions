"""Image Site Downloader

Go to a photo-sharing website Flickr and search for
a category of photos, download the resulting images.
"""

import re
import requests
from bs4 import BeautifulSoup

img_counter = 0

print("Accessing flickr..")
response = requests.get("https://www.flickr.com/search/?text=cute")
soup = BeautifulSoup(response.text, "html.parser")

print("Parsing flickr..")
# find style tags inside divs
for div in soup.find_all("div"):
    style = div.get("style")

    # if there is no style continue
    if style:
        continue
    # extract the url from the style
    match = re.search(r"(?<=url\().*?(?=(_\w)?.jpg\))", style)

    if match:
        # arrange the url according to Flickr standards
        photo_url = "https:" + match.group() + "_b.jpg"

        # download the pic
        pic = requests.get(photo_url)

        # if response is an unavailable image continue
        if pic.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable_l.png" or\
           pic.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable.png":
            continue
        # check for status errors
        pic.raise_for_status()

        # arrange photo file name
        photo_file = "Photos/photo{:03}.jpg".format(img_counter)

        # write the .jpg to the file
        with open(photo_file, "wb") as img_file:
            print("Writing to the file", photo_file)

            for chunk in pic.iter_content(100000):
                img_file.write(chunk)

            img_counter += 1
