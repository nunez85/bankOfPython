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


class Bank:

    def __init__(self) -> None:
        self.accounts = {}
        self.currentUser = None

    def promptForPassword(self):
        return input('Please enter your password: ')

    def promptForUserName(self):
        return input('Please enter your username: ')

    def login(self):
        username = self.promptForUserName()
        if username not in self.accounts:
            print('Unable to find your username')
            return

        user = self.accounts[username]
        password = self.promptForPassword()

        if password != user.password:
            print('Incorrect password!')
            return

        self.currentUser = user

        print()
        print(f'Welcome back, {user.username}!')

    def logout(self):
        print(
            f'Thanks for visiting Bank of Python {self.currentUser.username}.')
        print('Goodbye')
        print()
        self.currentUser = None
        print('Welcome to Bank of Python')

    def addAccount(self, newAccount):
        self.accounts[newAccount.username] = newAccount

    def createNewAccount(self):
        while True:
            username = input('Input new username: ')

            if username not in self.accounts:
                break
            elif username == '' or len(username) < 3:
                print(
                    'The username you entered is not valid. Please enter a username with at least 3 characters long')
            else:
                print('The username you entered already exists')

        while True:
            password = input('Input new password: ')

            if len(password) < 4:
                print(
                    'Invalid new password, please enter a password of at least 3 characters long')
            else:
                break

        newUser = BankAccount(username=username, password=password)
        self.accounts[username] = newUser
        self.currentUser = newUser
        print('New account successfully created!')
        print(f'Welcome to Bank Python {newUser.username}!')


def quit():
    print('Ok bye!')


def welcomeUser() -> None:
    print('Welcome to Bank of Python!')


def displayStartOptions() -> None:
    print()
    print('Press 1 to login if you already have an account')
    print('Press 2 to create a new account with us')
    print('Press q to quit this interaction')
    print()


def displayLoggedInOptions() -> None:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press s to show the account')
    print('Press w to make a withdrawal')
    print('Press l to logout')
    print('Press q to quit')
    print()


if __name__ == '__main__':
    bank = Bank()
    defaultAccount = BankAccount(username='isaac', password='hello')
    defaultAccount.balance = 1000
    bank.addAccount(defaultAccount)

    welcomeUser()

    while True:
        if bank.currentUser == None:
            displayStartOptions()
        else:
            displayLoggedInOptions()

        action = input('What do you want to do? ')
        action = action.lower()
        action = action[0]
        sleep(2)

        match action:
            case '1':
                bank.login()
            case '2':
                bank.createNewAccount()
            case 'b':
                bank.currentUser.showBalance()
            case 'd':
                bank.currentUser.deposit()
            case 'w':
                bank.currentUser.withdraw()
            case 's':
                bank.currentUser.showAccount()
            case 'l':
                bank.logout()
            case 'q':
                quit()
                break
            case _:
                print('Not a valid command!')

        sleep(2)
