CONTACTS_FILE = "contacts.txt"


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name and phone:
        with open(CONTACTS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{name} — {phone}\n")
        print("📞 Contact saved!")
    else:
        print("❌ Name and phone cannot be empty!")


def show_contacts():
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            contacts = file.readlines()
        if not contacts:
            print("📭 No contacts yet.")
            return
        print("\n📒 Contact Book:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact.strip()}")
    except FileNotFoundError:
        print("📭 Contact list is empty.")


def delete_contact():
    show_contacts()
    try:
        index = int(input("\nEnter number to delete: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            contacts = file.readlines()

        if 1 <= index <= len(contacts):
            removed = contacts.pop(index - 1)
            with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
                file.writelines(contacts)
            print(f"🗑 Deleted: {removed.strip()}")
        else:
            print("❌ No contact with that number!")
    except FileNotFoundError:
        print("📭 Contact list is empty.")


def main():
    print("📱 Contact Book")
    print("1 — Add contact")
    print("2 — Show contacts")
    print("3 — Delete contact")
    print("4 — Exit")

    while True:
        choice = input("\nChoose option (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option!")


if __name__ == "__main__":
    main()
