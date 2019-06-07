import datetime as dt
import math

f = open("employees.txt", "rt")
employees = []
for line in f:
    parts = line.strip("\n").split(",")
    if len(parts) < 3:
        continue
    try:
        sdate = dt.datetime.strptime(parts[2], "%d-%m-%Y")

        if len(parts) == 3:
            edate = dt.datetime.now()
        else:
            edate = dt.datetime.strptime(parts[3], "%d-%m-%Y")

        years = math.floor((edate - sdate).days / 365)

        # print(f"{parts[0]:10}  {parts[1]:10}  {years:2}")
        employees.append((parts[0], parts[1], years))
    except:
        pass

for e in sorted(employees, key=lambda t: t[2], reverse=True):
    print(f"{e[0]:10}  {e[1]:10}  {e[2]:2}")
