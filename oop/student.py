class Student:
    def __init__(self, admno, name):
        self.admno = admno
        self.name = name

    def print_details(self):
        print("Admno  :", self.admno)
        print("Name   :", self.name)


class PythonStudent(Student):
    def __init__(self, admno, name, labmarks):
        super().__init__(admno, name)
        self.labmarks = labmarks

    # Overriding
    def print_details(self):
        super().print_details()
        print("Lab marks : ", self.labmarks)

    def get_result(self):
        if self.labmarks >= 75:
            return "Pass"
        else:
            return "Fail"


class OracleStudent(Student):
    def __init__(self, admno, name, theorymarks):
        super().__init__(admno, name)
        self.theorymarks = theorymarks

    # Overriding
    def print_details(self):
        super().print_details()
        print("Theory marks : ", self.theorymarks)

    def get_result(self):
        if self.theorymarks >= 50:
            return "Pass"
        else:
            return "Fail"


ps = PythonStudent(1, "Abc", 80)
ps.print_details()
print("Result = ", ps.get_result())
