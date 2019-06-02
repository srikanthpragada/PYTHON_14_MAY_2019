class Marks:
    def __init__(self):
        self.marks = [20, 30, 40, 25, 66]

    def __iter__(self):
        self.pos = 0  # start at 0 to iterate again
        return self

    def __next__(self):
        if self.pos == len(self.marks):
            raise StopIteration
        else:
            self.pos += 1

        return self.marks[self.pos - 1]

m = Marks()
mi1 = iter(m)
mi2 = iter(m)

print( mi1.__next__())
print( mi2.__next__())

