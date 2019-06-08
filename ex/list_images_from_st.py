import requests
from bs4 import BeautifulSoup
import sys

resp = requests.get("http://www.flipkart.com")
if resp.status_code != 200:
     print("Sorry! Could not get details")
     sys.exit(0)

bs = BeautifulSoup(resp.text,"html.parser")
images = bs.find_all("img")

for t in images:
    if 'src' in t.attrs:
        print(t['src'])



