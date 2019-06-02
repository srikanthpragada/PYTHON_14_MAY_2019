f = open("mobile.txt","rt")
mobiles = []
for line in f:
    numbers = line.strip("\n").split(",")
    for n in numbers:
        if len(n) == 10 and n.isdigit():
            mobiles.append(n)

for n in sorted(mobiles):
    print(n)



