# takes input on command line

import sys

if len(sys.argv) < 2:
    print("Number is missing")
    sys.exit(1)


num = int(sys.argv[1])

fact = 1
for n in range(1,num + 1):
    fact *= n

print(f"Factorial of {num} is {fact}")
