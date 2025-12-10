import random

def flip_coin():
    return "🦅 Heads" if random.choice([True, False]) else "🌑 Tails"

def main():
    print("🪙 Coin Flip Simulator")
    while True:
        choice = input("\nPress Enter to flip the coin or type 'q' to quit: ").strip().lower()
        if choice == "q":
            print("👋 Bye!")
            break
        print("Flipping...")
        result = flip_coin()
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
