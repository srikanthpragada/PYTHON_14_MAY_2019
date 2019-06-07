import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries")
    sys.exit(1)

countries = resp.json()
top10 = sorted(countries, key=lambda d: d['population'], reverse=True)[:10]

for i,c in enumerate(top10,1):
    print(f"{i}:{c['name']:30} - {c['population']:15}")
