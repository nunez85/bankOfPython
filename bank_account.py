from sys import stdout
from time import sleep


class BankAccount:

    def __init__(self, username, password) -> None:
        self.balance = 0
        self.username = username
        self.password = password

    def showAmountError():
        print('Unable to parse amount entered, please enter a number > 0')

    def showBalance(self):
        print(f'Your balance is ${self.balance}.')

    def deposit(self):
        depositAmount = input('Please enter amount to deposit: $')
        try:
            depositAmount = int(depositAmount)
        except:
            self.showAmountError()

        if depositAmount < 0:
            self.showAmountError()

        else:
            self.balance += depositAmount
            print(f'Your new balance is ${self.balance}')

    def withdraw(self):
        withdrawalAmount = input('Please enter amount to withdraw: $')

        try:
            withdrawalAmount = int(withdrawalAmount)
        except:
            self.showAmountError()

        if withdrawalAmount > self.balance:
            print(
                f"You can't withdraw more money than your balance => ${self.balance}")
            return

        self.balance -= withdrawalAmount
        stdout.write('Retrieving your money')
        stdout.flush()
        sleep(1)

        seconds = 3
        while seconds > 0:
            stdout.write('.')
            stdout.flush()
            sleep(1)
            seconds -= 1
        print()
        stdout.flush()
        print(f'New balance => ${self.balance}')

    def showAccount(self):
        print(f'Username => {self.username}')
        print(f'Balance => ${self.balance}')
