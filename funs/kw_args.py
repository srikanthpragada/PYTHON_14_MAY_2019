def fun(v, *options, **values):
    print(type(values))


fun(10, 20,30,50, x=10,y=20,a="Abc",done=True)

