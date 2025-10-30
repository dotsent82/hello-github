import random
from datetime import datetime

TIPS = [
    "Small steps daily beat big plans someday.",
    "Name your commits clearly – future you will thank you.",
    "Break problems into tiny pieces.",
    "Reading error messages saves hours.",
]

def ask_int(prompt: str) -> int:
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Введите целое число, попробуем ещё раз.")

def calc_sum():
    a = ask_int("Первое число: ")
    b = ask_int("Второе число: ")
    print(f"Сумма: {a + b}")

def greet():
    name = input("Как тебя зовут? > ")
    print(f"Привет, {name}! Рад знакомству 👋")

def tip():
    print("Совет:", random.choice(TIPS))

def save_note():
    text = input("Введи заметку: ")
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}\n")
    print("Заметка сохранена в notes.txt")

def show_menu():
    print("\n=== Меню ===")
    print("1) Приветствие")
    print("2) Сложить два числа")
    print("3) Случайный совет")
    print("4) Сохранить заметку в файл")
    print("0) Выход")

def main():
    print("Добро пожаловать в консольное приложение!")
    while True:
        show_menu()
        choice = input("Выбор: ").strip()
        if choice == "1":
            greet()
        elif choice == "2":
            calc_sum()
        elif choice == "3":
            tip()
        elif choice == "4":
            save_note()
        elif choice == "0":
            print("Пока! 👋")
            break
        else:
            print("Неизвестная команда. Выбери пункт из меню.")

if __name__ == "__main__":
    main()
