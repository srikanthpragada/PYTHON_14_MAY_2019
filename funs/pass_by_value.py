def fun(n):
    print(id(n))
    n = 0
    print(id(n))


a = 10
print(id(a))
fun(a)
print(a)


