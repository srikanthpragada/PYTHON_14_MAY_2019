class Account:
    # static or class attributes
    minbal = 5000

    # Constructor
    def __init__(self, acno, customer, balance=0):
        # Object attributes
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    @staticmethod
    def get_minbal():
        return Account.minbal

    def __str__(self):
        return f"{self.acno} - {self.customer} - {self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno

    def __gt__(self, other):
        return self.balance > other.balance

    @property
    def current_balance(self):
        return self.balance

if __name__ == '__main__':
    a1 = Account(1, "Scott", 15000)  # Object
    print(a1.current_balance)  #property
    a2 = Account(2, "Steve", 10000)

    print(a1 == a2)  # a1.__eq__(a2)
    print(a1 > a2)

    print(str(a1))  # a1.__str__()

    a1.deposit(50000)
    print(a1.get_balance())
    print(Account.get_minbal())
