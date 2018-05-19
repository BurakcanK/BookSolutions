""" Scheduled Web Comic Downloader

Modified version of ImageDownloader.py from Chapter11

Checks the given url and automatically downloads the images since the program's last visit.
Code is written so that it runs on Ubuntu, using cron.

You need to configure cron to run this script everyday on a specific time.
Below is a crontab job to be run at 15:00 o'clock every day.

You can edit your file with the command `crontab -e`, and then add the following line.

0 15 * * * /usr/bin/python3 /<path to your folder>/Schedule/schedule.py > /<path to your folder>/Schedule/crontab.log 2>&1
"""

import re
import requests
import sys
from bs4 import BeautifulSoup

imgCounter = 0

response = requests.get("https://www.flickr.com/search/?text=webcomic")
soup = BeautifulSoup(response.text, 'html.parser')

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

        # abs path to the location for images to be downloaded
        abspathPhotos = "/<path to your folder>/Schedule/Photos"

        # arrange photo file name
        photoFile = '{}/photo{:03}.jpg'.format(abspathPhotos, imgCounter)

        # write the .jpg to the file
        with open(photoFile, 'wb') as imgFile:
            for chunk in pic.iter_content(100000):
                imgFile.write(chunk)

            imgCounter += 1
