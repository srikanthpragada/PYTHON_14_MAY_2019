import sys

import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries")
    sys.exit(1)

countries = resp.json()

for c in countries:
    if c['population'] is not None and c['area'] is not None:
        c['den'] = round(c['population'] / c['area'])
    else:
        c['den'] = 0


top10 = sorted(countries, key=lambda d: d['den'], reverse=True)[:10]

print("\nTop 10 based on density\n")

for i, c in enumerate(top10, 1):
    print(f"{i:2}:{c['name']:50} - {c['den']:5}")

countries = filter(lambda c: c['den'] != 0, countries)
top10 = sorted(countries, key=lambda d: d['den'])[:50]


print("\nBottom 10 based on density\n")

for i, c in enumerate(top10, 1):
    print(f"{i:2}:{c['name']:50} - {c['den']:5}")
