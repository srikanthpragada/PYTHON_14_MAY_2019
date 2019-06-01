class EvenNums_Iterator:
    def __init__(self):
        self.start = 2

    def __next__(self):
        if self.start > 10:
            raise StopIteration
        else:
            self.start += 2
            return self.start - 2

class EvenNums:
    def __iter__(self):
        return EvenNums_Iterator()

for n in EvenNums():
    print(n)
