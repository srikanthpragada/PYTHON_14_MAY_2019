dir = {}

while True:
    name = input("Enter name [end to stop] : ")
    if name == 'end':
        break

    mobile = input ("Enter Mobile Number :")
    if name in dir:   # if name already present
        dir[name].add(mobile)
    else:
        dir[name] = {mobile}  # add key and set of mobiles

for n,m in sorted(dir.items()):
    print(f"{n:10s} {','.join(sorted(m))}")




