""" Image Site Downloader

This script goes to a photo-sharing website Flickr and searches for
a category of photos, downloads the resulting images.
"""

import sys, requests, re
from bs4 import BeautifulSoup

imgCounter = 0

print("Accessing flickr..")
response = requests.get("https://www.flickr.com/search/?text=cute")
soup = BeautifulSoup(response.text, 'html.parser')

print("Parsing flickr..")
# find style tags inside divs
for div in soup.find_all('div'):
    style = div.get('style')

    # if there is no style continue
    if style == None:
        continue
    # extract the url from the style
    match = re.search(r'(?<=url\().*?(?=(_\w)?.jpg\))', style)

    if match:
        # arrange the url according to Flickr standards
        photoUrl = 'https:' + match.group() + "_b.jpg"

        # download the pic
        pic = requests.get(photoUrl)

        # if response is an unavailable image continue
        if pic.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable_l.png" or\
           pic.url == "https://s.yimg.com/pw/images/en-us/photo_unavailable.png":
            continue
        # check for status errors
        pic.raise_for_status()

        # arrange photo file name
        photoFile = 'Photos/photo{:03}.jpg'.format(imgCounter)

        # write the .jpg to the file
        with open(photoFile, 'wb') as imgFile:
            print("Writing to the file", photoFile)

            for chunk in pic.iter_content(100000):
                imgFile.write(chunk)

            imgCounter += 1