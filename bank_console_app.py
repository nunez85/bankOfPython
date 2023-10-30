from time import sleep
from bank_account import BankAccount
from bank import Bank


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
        sleep(1)

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
