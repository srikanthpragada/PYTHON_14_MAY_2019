import requests
import sys

user = input("Enter git username : ")
url = f"https://api.github.com/users/{user}/repos"

resp = requests.get(url)
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    sys.exit(0)

repos = resp.json()

for repo in repos:
    print(repo["name"])
