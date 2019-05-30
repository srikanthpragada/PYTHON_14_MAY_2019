class A:
    def process(self):
        print("A process()")

    def task(self):
        print("A task()")


class B:
    def process(self):
        print("B process()")

    def task(self):
        print("B task()")

class C(B, A):
    def process(self):
        print("C process()")


obj = C()
print(C.mro())
obj.process()
obj.task()
