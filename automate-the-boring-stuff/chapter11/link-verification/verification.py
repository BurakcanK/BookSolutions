"""Link Verification

Given the URL of a webpage, the program will attempt to download every linked
page on the webpage and print the pages that returns 404 code in the response.

Usage:
    python3 verification.py <url>
"""

import requests
import sys
from bs4 import BeautifulSoup

# ensure usage
if len(sys.argv) == 1:
    url = "https://www.gov.uk/404"
elif len(sys.argv) == 2:
    url = sys.argv[1]
else:
    print("Usage: python3 verification.py <url>")
    sys.exit()

# go to url and parse it
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# find all anchors
for anchor in soup.find_all("a"):
    # extract the link from the anchor
    link = anchor.get("href")
    if not link.startswith("http"):
        link = url + link

    if requests.get(link).status_code == 404:
        print("404 error from ->", link)
