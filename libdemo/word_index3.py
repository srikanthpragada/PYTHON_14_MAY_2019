f = open("test.txt", "rt")
word_index = {}
for lineno, line in enumerate(f.readlines(), 1):
    wrds = line.split()
    for w in wrds:
        w = w.strip("\n.")
        if w in word_index:
            word_index[w].add(lineno)
        else:
            word_index[w] = {lineno}

f.close()
for w, index in sorted(word_index.items()):
    print(f"{w:10} {index}")
