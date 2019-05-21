def iseven(n):
    return n % 2 == 0


nums = [11, 10, 80, 55, 66]

# for n in filter(iseven,nums):
#     print(n)

for n in filter(lambda n : n % 2 == 0, nums):
    print(n)
