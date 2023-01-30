import random
import string


def generate_password(length, format="default"):
  charset = ""

  if format == "default":
    charset = string.ascii_letters + string.digits + string.punctuation
  elif format == "easy":
    charset = string.ascii_letters + string.digits
  elif format == "letters_only":
    charset = string.ascii_letters
  elif format == "digits_only":
    charset = string.digits

  password = "".join(random.choice(charset) for i in range(length))

  return password


length = int(input("Enter the password length (minimum 6):\n"))

print("Choose password format:")
print("1. Default (letters, digits, and symbols)")
print("2. Easy (letters and digits only)")
print("3. Letters only")
print("4. Digits only")

format = int(input("Enter your choice (1-4):\n"))

if format == 1:
  password = generate_password(length, "default")
elif format == 2:
  password = generate_password(length, "easy")
elif format == 3:
  password = generate_password(length, "letters_only")
elif format == 4:
  password = generate_password(length, "digits_only")
else:
  password = generate_password(length, "default")

print("Generated password:", password)
input("Press Enter to Exit")
