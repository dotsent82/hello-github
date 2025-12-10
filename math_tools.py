def square(number: float) -> float:
    """Возвращает квадрат числа."""
    return number ** 2


def cube(number: float) -> float:
    """Возвращает куб числа."""
    return number ** 3


def factorial(n: int) -> int:
    """Возвращает факториал числа n (n!)."""
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def percent(part: float, whole: float) -> float:
    """Возвращает процент от числа: part из whole."""
    if whole == 0:
        raise ValueError("Нельзя делить на ноль")
    return (part / whole) * 100


def main():
    print("📐 Math Tools")
    print("1 — square (квадрат числа)")
    print("2 — cube (куб числа)")
    print("3 — factorial (факториал)")
    print("4 — percent (проценты)")
    print("5 — exit")

    while True:
        choice = input("\nChoose option (1-5): ")

        if choice == "1":
            num = float(input("Enter number: "))
            print(f"Result: {square(num)}")
        elif choice == "2":
            num = float(input("Enter number: "))
            print(f"Result: {cube(num)}")
        elif choice == "3":
            n = int(input("Enter integer n >= 0: "))
            try:
                print(f"Result: {factorial(n)}")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "4":
            part = float(input("Enter part: "))
            whole = float(input("Enter whole: "))
            try:
                print(f"Result: {percent(part, whole):.2f}%")
            except ValueError as e:
                print(f"❌ Error: {e}")
        elif choice == "5":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")


if __name__ == "__main__":
    main()
