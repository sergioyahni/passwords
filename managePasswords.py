import json
import pyperclip
from functions import generate, validPassword, checkIfItemExists,encode, decode


class Passwords:
    savedData = r"\absolute\path\to\data.json"

    def __init__(self, website=None, user=None):
        self.password = None
        self.website = website
        self.user = user

    def savePassword(self, password=None):
        self.password = generate() if password is None else password
        if checkIfItemExists(self.website):
            print("Data to be saved:")
            print(f"Website: {self.website}\nUser:{self.user}\nPassword: {self.password}")
            if validPassword(self.password):
                new_data = {
                    self.website: {
                        "user": encode(self.user),
                        "password": encode(self.password)
                    }
                }

                try:
                    with open("data.json", "r") as datafile:
                        data = json.load(datafile)

                except FileNotFoundError:
                    with open("data.json", "w") as datafile:
                        json.dump(new_data, datafile, indent=4)

                else:
                    data.update(new_data)
                    with open("data.json", "w") as datafile:
                        json.dump(data, datafile, indent=4)
            else:
                print("Sorry, the password is  not valid.")
        else:
            print("Website is already in records.")

    def searchPassword(self):
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
                user = decode(data[self.website]['user'])
                password = decode(data[self.website]['password'])
                pyperclip.copy(password)
                print(f"USER: {user}\nPASSWORD: {password}\nThe password was copied to the clipboard.")

        except FileNotFoundError:
            print("Record was not found")
        except KeyError:
            print("Record was not found")

    def showAllpassword(self):
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
            for key in data:
                print(f"{key}\t{decode(data[key]['user'])}\t{decode(data[key]['password'])}")

        except FileNotFoundError:
            print("File not found")

    def DeletePassword(self):
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
            del data[self.website]

            with open("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)

        except FileNotFoundError:
            print("File not found")


if __name__ == "__main__":
    p = Passwords("sergio.com", "sergio@mail.com")
    p.DeletePassword()
