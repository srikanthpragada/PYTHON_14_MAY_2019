def add(n1, n2):
    return n1 + n2


def message(msg="Hello", name="Guest"):
    print(msg + " " + name)


print(add(10, 20))
print(add(n2=1,n1=10))

message("Welcome","Scott")
message("Good morning")
message()
message(name="Scott", msg="Good Bye")


