import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_user_choice():
    while True:
        choice = input("Choose rock ✊, paper ✋ or scissors ✌: ").lower()
        if choice in CHOICES:
            return choice
        print("❌ Invalid choice. Try again!")

def decide_winner(user, computer):
    if user == computer:
        return "🤝 It's a tie!"

    if (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "🎉 You win!"
    
    return "😢 You lose!"

def main():
    print("🎮 Rock-Paper-Scissors Game")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"🧍 You: {user}")
        print(f"💻 Computer: {computer}")
        print(decide_winner(user, computer))

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("👋 Bye!")
            break

if __name__ == "__main__":
    main()
