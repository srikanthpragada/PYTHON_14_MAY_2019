# List broken links from www.srikanthtechnologies.com

import requests
from bs4 import BeautifulSoup
import sys
import datetime as dt

URL = "http://www.srikanthtechnologies.com"
resp = requests.get(URL)
if resp.status_code != 200:
     print("Sorry! Could not get details")
     sys.exit(0)

bs = BeautifulSoup(resp.text,"html.parser")
anchors = bs.find_all("a")
links = set()
for t in anchors:
    if 'href' in t.attrs:
        links.add( t['href'])

# Prepend website to links that are relative urls
newlinks = set()
for link in links:
    if link.startswith("http"):
        newlinks.add(link)
    else:
        # add URL
        newlinks.add( URL + "/" + link)

f = open("borken_links_" + str(dt.date.today()) + ".txt","wt")
for link in newlinks:
    resp = requests.get(link)

    if resp.status_code != 200:  # Broken link
        print(link)
        f.write(link + "\n")


f.close()
print("Done")


