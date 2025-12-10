def calculate():
    print("🧮 Simple GitHub Calculator")
    print("Choose operation:")
    print("1 — Add")
    print("2 — Subtract")
    print("3 — Multiply")
    print("4 — Divide")

    choice = input("Enter number of operation (1-4): ")

    if choice not in {"1", "2", "3", "4"}:
        return "❌ Invalid choice!"

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = a + b
    elif choice == "2":
        result = a - b
    elif choice == "3":
        result = a * b
    else:
        if b == 0:
            return "❌ Division by zero is impossible!"
        result = a / b

    return f"Result: {result}"

if __name__ == "__main__":
    print(calculate())
