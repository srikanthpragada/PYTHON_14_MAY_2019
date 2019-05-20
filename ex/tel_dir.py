dir = {}

while True:
    name = input("Enter name [end to stop] : ")
    if name == 'end':
        break

    mobile = input ("Enter Mobile Number :")
    dir[name] = mobile

for n,m in  dir.items():
    print(f"{n:10s} {m}")




