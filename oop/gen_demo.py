
# Generator to generate even numbers from 2 to 10
def even_nums():
    for i in range(2,11,2):
        yield  i


for n in even_nums():
    print(n)
