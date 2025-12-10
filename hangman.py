import random

WORDS = [
    "python",
    "github",
    "developer",
    "commit",
    "variable",
    "function",
    "terminal",
    "keyboard",
    "algorithm",
    "project",
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]


def choose_word():
    return random.choice(WORDS)


def display_state(secret_word, guessed_letters, attempts_left):
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts_left])
    print("\nWord: ", end="")
    display = [
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ]
    print(" ".join(display))
    print(f"\nGuessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print(f"Attempts left: {attempts_left}")


def hangman():
    print("🎮 Hangman Game (Виселица)")
    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = len(HANGMAN_PICS) - 1

    while attempts_left > 0:
        display_state(secret_word, guessed_letters, attempts_left)

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter ONE letter (a-z).")
            continue

        if guess in guessed_letters:
            print("⚠ You already tried that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Good job! Letter is in the word.")
            if all(letter in guessed_letters for letter in secret_word):
                print("\n🎉 You WIN! The word was:", secret_word)
                return
        else:
            print("❌ No such letter in the word.")
            attempts_left -= 1

    display_state(secret_word, guessed_letters, attempts_left)
    print("\n💀 You LOST! The word was:", secret_word)


if __name__ == "__main__":
    hangman()
