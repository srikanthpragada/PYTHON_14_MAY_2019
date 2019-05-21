def fun():
    print("In  fun()")


def add(a, b):
    return a + b


def mathop(fun, n1, n2):
    return fun(n1,n2)


print(mathop(add, 10, 20))

fun2 = fun
print(type(fun))
print(id(fun), id(fun2))

fun()
fun2()
