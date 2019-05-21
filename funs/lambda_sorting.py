names = ["Java", "python", "c", "TS", "Kotlin"]

for n in sorted(names,key=len):
    print(n)

print("Case Insensitive sorting")

# for n in sorted(names,key=str.upper):
#     print(n)

for n in sorted(names,key=lambda v : v.upper()):
    print(n)

