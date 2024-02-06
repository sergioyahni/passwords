from random import choice, randint, shuffle
import re
import json
import base64


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    return "".join(password_list)


def validPassword(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    match = re.match(pattern, password)
    return bool(match)


def checkIfItemExists(website):
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
        if website in data:
            return False
        else:
            return True
    except FileNotFoundError:
        return True


def encode(text):
    textBytes = text.encode("ascii")
    base64Bytes = base64.b64encode(textBytes)
    return base64Bytes.decode("ascii")


def decode(b64Text):
    base64_bytes = b64Text.encode("ascii")
    b64TextBytes = base64.b64decode(base64_bytes)
    return  b64TextBytes.decode("ascii")
