
# A simple program to simulate your bank account with withdrawing and deposit functions. Code available


class BankAccount:
    acc_number = 1

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.acc_number = BankAccount.acc_number
        BankAccount.acc_number = BankAccount.acc_number+1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def with_draw(self, amount):
        if amount < self.balance:
            print('Not Enough Balance')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance


