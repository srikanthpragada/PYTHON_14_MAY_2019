import os

for f in os.walk(".."):
    if f[0].find(".git") >= 0:
        continue

    print(f"{f[0]:20} -  {len(f[1])} -  {len(f[2])}")
