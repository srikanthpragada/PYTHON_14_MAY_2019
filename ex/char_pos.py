
s1 = "This-is-fine"
s2 = "How is it"

for c in s2:
    pos = s1.find(c)
    if pos >= 0:
        print("Found at : " , pos)
        break
else:
    print("Not Found")

