import random
import string


def generate_password(length, charset=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(charset) for i in range(length))


def get_length():
    while True:
        try:
            length = int(input("Enter the password length (minimum 6):\n"))
            if length >= 6:
                return length
            print("Password length must be at least 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_charset():
    charset = input("Enter a custom character set (optional):\n")
    return charset if charset else string.ascii_letters + string.digits + string.punctuation


if __name__ == '__main__':
    length = get_length()
    charset = get_charset()
    password = generate_password(length, charset)
    print("Generated password:", password)
