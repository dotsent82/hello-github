ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        lower = ch.lower()
        if lower in ALPHABET:
            idx = ALPHABET.index(lower)
            new_idx = (idx + shift) % len(ALPHABET)
            new_char = ALPHABET[new_idx]
            # сохраняем регистр
            result.append(new_char.upper() if ch.isupper() else new_char)
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


def main():
    print("🔐 Simple Caesar Cipher")
    print("1 — Encrypt text")
    print("2 — Decrypt text")
    print("3 — Exit")

    while True:
        choice = input("\nChoose option (1-3): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            try:
                shift = int(input("Shift (e.g. 3): "))
            except ValueError:
                print("❌ Shift must be a number.")
                continue
            encrypted = caesar_encrypt(text, shift)
            print(f"\n🔒 Encrypted:\n{encrypted}")
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            try:
                shift = int(input("Shift (same number used to encrypt): "))
            except ValueError:
                print("❌ Shift must be a number.")
                continue
            decrypted = caesar_decrypt(text, shift)
            print(f"\n🔓 Decrypted:\n{decrypted}")
        elif choice == "3":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")


if __name__ == "__main__":
    main()
