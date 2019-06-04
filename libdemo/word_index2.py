
f = open("test.txt","rt")
word_count = {}
for line in f:
    wrds = line.split()
    for w in wrds:
        w = w.strip("\n.")
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

f.close()

print(word_count)





