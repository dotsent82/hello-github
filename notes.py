NOTES_FILE = "notes.txt"

def add_note():
    note = input("Write your note: ")
    if note.strip():
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("📝 Note saved!")
    else:
        print("❌ Empty note not saved.")

def show_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.readlines()
        if not notes:
            print("📭 No notes found.")
            return
        print("\n📒 Your notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("📭 No notes file yet.")

def main():
    print("🗂 Notes App")
    print("1 — Add note")
    print("2 — Show notes")
    print("3 — Exit")

    while True:
        choice = input("\nChoose option (1-3): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")

if __name__ == "__main__":
    main()
