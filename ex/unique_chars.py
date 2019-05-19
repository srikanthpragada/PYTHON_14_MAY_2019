
st = input("Enter a string : ")
chars = set()   # Empty set

for c in st:
   chars.add(c)


for c in sorted(chars):
    print(c)


