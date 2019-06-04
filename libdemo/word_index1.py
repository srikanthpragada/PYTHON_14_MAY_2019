
f = open("test.txt","rt")
words = set()
for line in f:
    wrds = line.split()
    for w in wrds:
        words.add(w.strip("\n."))

f.close()

print(words)





