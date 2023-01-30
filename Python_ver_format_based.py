import random
import re


def generatePassword(format):
    password = ""
    pattern = re.compile(r"\[(?P<group>[a-zA-Z]+)\((?P<length>\d+)\)\]")
    start = 0
    for group_match in pattern.finditer(format):
        password += format[start:group_match.start()]
        group = group_match.group("group")
        length = int(group_match.group("length"))
        if group == "symbols":
            chars = "!@#$%^&*"
        elif group == "numbers":
            chars = "0123456789"
        elif group == "lcharacters":
            chars = "abcdefghijklmnopqrstuvwxyz"
        elif group == "ucharacters":
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        for i in range(length):
            password += random.choice(chars)
        start = group_match.end()
    password += format[start:]
    return password


format = input("Enter custom format (e.g. <input>[symbols(1)]<input>[numbers(1)]<input>[lcharacters]<input>[ucharacters]):\n")
print("Generated password: ", generatePassword(format))
input("Press Enter to Exit")
