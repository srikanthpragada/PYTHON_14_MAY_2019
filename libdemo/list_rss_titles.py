import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")

# must install lxml to use xml
soup = BeautifulSoup(resp.text, "xml")
for item in soup.find_all("item"):
    print(item.find("title").get_text().strip(" "))
