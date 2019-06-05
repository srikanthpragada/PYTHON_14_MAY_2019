import os


def display_file(filename):
    print("-" * 80)
    print("Filename : ", filename)
    print("-" * 80)
    f = open(filename, "rt")
    for line in f:
        print(line, end='')


files = os.listdir()
for f in files:
    if f.endswith(".py"):
        display_file(f)
