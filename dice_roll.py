import random
import time

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Dice Roll Simulator")
    while True:
        choice = input("\nPress Enter to roll the dice or type 'q' to quit: ").strip().lower()
        if choice == "q":
            print("👋 Bye!")
            break

        print("Rolling...")
        time.sleep(1)
        result = roll_dice()
        print(f"🎯 You rolled: {result}")

if __name__ == "__main__":
    main()
