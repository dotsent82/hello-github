import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter password length (8-32): "))
        if length < 8 or length > 32:
            print("⚠ Length must be between 8 and 32. Using default = 12.")
            length = 12
    except ValueError:
        print("⚠ Invalid input. Using default length = 12.")
        length = 12

    new_password = generate_password(length)
    print("\nYour new password:")
    print(f"🔑 {new_password}")

if __name__ == "__main__":
    main()
