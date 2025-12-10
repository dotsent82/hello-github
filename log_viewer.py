import os

DEFAULT_LOG_FILE = "app.log"


def choose_file():
    print(f"📄 Default log file: {DEFAULT_LOG_FILE}")
    choice = input("Press Enter to use default or type another filename: ").strip()
    return choice if choice else DEFAULT_LOG_FILE


def show_last_lines(filename: str, lines: int = 10):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found.")
        return

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        content = f.readlines()

    if not content:
        print("📭 File is empty.")
        return

    print(f"\n📌 Last {lines} lines of '{filename}':\n")
    for line in content[-lines:]:
        print(line.rstrip())


def search_in_file(filename: str, keyword: str):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found.")
        return

    print(f"\n🔍 Searching for '{keyword}' in '{filename}':\n")
    found = False

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                print(f"[line {i}] {line.rstrip()}")
                found = True

    if not found:
        print("📭 Nothing found.")


def main():
    print("📜 Log Viewer")
    filename = choose_file()

    while True:
        print("\nMenu:")
        print("1 — Show last 10 lines")
        print("2 — Show last N lines")
        print("3 — Search by keyword")
        print("4 — Change file")
        print("5 — Exit")

        choice = input("\nChoose option (1-5): ").strip()

        if choice == "1":
            show_last_lines(filename, 10)
        elif choice == "2":
            try:
                n = int(input("How many last lines to show? "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue
            show_last_lines(filename, n)
        elif choice == "3":
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                search_in_file(filename, keyword)
            else:
                print("❌ Keyword cannot be empty.")
        elif choice == "4":
            filename = choose_file()
        elif choice == "5":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")


if __name__ == "__main__":
    main()
