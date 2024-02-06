from managePasswords import Passwords
import sys


def save(website, user, password=None):
    action = Passwords(website, user)
    action.savePassword(password)


def delete(website):
    action = Passwords(website)
    action.DeletePassword()


def search(website):
    action = Passwords(website)
    action.searchPassword()


def show():
    print("\n")
    action = Passwords()
    action.showAllpassword()
    print("\n")


def help():
   print(helpText)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        password = None
        if len(sys.argv) > 4:
            password = sys.argv[4]
        eval(sys.argv[1])(sys.argv[2], sys.argv[3], password)

    elif len(sys.argv) > 2:
        eval(sys.argv[1])(sys.argv[2])

    elif len(sys.argv) == 2:
        eval(sys.argv[1])()

    else:
        raise "You are missing arguments to proceed."
