tasks = []

def show_menu():
    print("\n✅ TODO List")
    print("1 — Add task")
    print("2 — Show tasks")
    print("3 — Delete task")
    print("4 — Exit")

def add_task():
    task = input("Enter new task: ")
    if task.strip():
        tasks.append(task)
        print("➕ Task added!")
    else:
        print("❌ Empty task not added.")

def show_tasks():
    if not tasks:
        print("📭 No tasks yet.")
        return
    print("\n📋 Your tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    if not tasks:
        print("📭 No tasks to delete.")
        return

    show_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑 Deleted: {removed}")
        else:
            print("❌ No task with that number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")

if __name__ == "__main__":
    main()
