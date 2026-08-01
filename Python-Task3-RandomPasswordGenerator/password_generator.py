import random
import string

print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password must be at least 8 characters long.\n")
            continue

        print("\nSelect character types:")
        upper = input("Include Uppercase letters? (y/n): ").lower() == "y"
        lower = input("Include Lowercase letters? (y/n): ").lower() == "y"
        digits = input("Include Numbers? (y/n): ").lower() == "y"
        symbols = input("Include Symbols? (y/n): ").lower() == "y"

        selected = []

        if upper:
            selected.append(string.ascii_uppercase)
        if lower:
            selected.append(string.ascii_lowercase)
        if digits:
            selected.append(string.digits)
        if symbols:
            selected.append(string.punctuation)

        if len(selected) < 2:
            print("\nPlease select at least TWO character types.\n")
            continue

        password = []

        for chars in selected:
            password.append(random.choice(chars))

        all_characters = "".join(selected)

        while len(password) < length:
            password.append(random.choice(all_characters))

        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using Random Password Generator!")
            break

    except ValueError:
        print("\nPlease enter a valid number.\n")
