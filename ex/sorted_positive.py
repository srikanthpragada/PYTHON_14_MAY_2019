lst = []

while True:
    num = int(input("Enter a number [0 to stop ]:"))
    if num == 0:
        break

    if num > 0:
        lst.append(num)

for n in sorted(lst):
    print(n, end = ' ')