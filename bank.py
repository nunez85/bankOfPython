from bank_account import BankAccount


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

            if len(password) < 3:
                print(
                    'Invalid new password, please enter a password of at least 3 characters long')
            else:
                break

        newUser = BankAccount(username=username, password=password)
        self.accounts[username] = newUser
        self.currentUser = newUser
        print('New account successfully created!')
        print(f'Welcome to Bank Python {newUser.username}!')
