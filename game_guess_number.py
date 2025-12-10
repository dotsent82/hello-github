import random

def guess_number():
    print("🎮 Welcome to *Guess the Number!*")
    print("I'm thinking of a number from 1 to 20...")

    number = random.randint(1, 20)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guess == number:
            return "🎉 Correct! You guessed the number!"

        attempts -= 1

        if guess < number:
            print("🔼 Too low!")
        else:
            print("🔽 Too high!")

        print(f"Attempts left: {attempts}")

    return f"😢 No attempts left! The number was {number}."

if __name__ == "__main__":
    print(guess_number())
