import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries")
    sys.exit(1)

countries = resp.json()
print("No. of countries : ", len(countries))
for c in countries:
    print(f"{c['name'][:50]:50}  {c['capital']}")