
def factorials(lst):
    for n in lst:
        fact = 1
        for i in range(2,n+1):
            fact *= i

        yield  fact


for f in factorials([1,4,7]):
    print(f)




