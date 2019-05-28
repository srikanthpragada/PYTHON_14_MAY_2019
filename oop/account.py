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

    def get_minbal(self):
        return self.minbal


a1 = Account(1, "Scott")  # Object
a2 = Account(2, "Tim", 10000)

a1.deposit(50000)
a1.deposit(10000)
print(a1.get_balance())
print(a1.get_minbal())
