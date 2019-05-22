g = 10  # Global variable

def fun1():
    a = 100  # Enclosing variable
    # Local function
    def fun2():
        nonlocal a
        b = 200  # Local variable
        a = a  +  1
        print(g, a, b)

    fun2()
    print(a)

fun1()
