import re

f = open("mobile_numbers.txt","rt")
mobiles = []
for line in f:
    numbers = re.findall("\d+",line)
    for m in numbers:
        if len(m) == 10:
           mobiles.append(m)


for n in sorted(mobiles):
    print(n)



