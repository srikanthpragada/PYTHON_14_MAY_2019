def add(lst, n):
    lst.append(n)
    print(id(lst))
    # lst = []
    lst.clear()
    print(id(lst))


l = [10, 20]
add(l, 30)
print(l)
