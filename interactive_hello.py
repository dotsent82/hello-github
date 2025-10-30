import random

name = input("What's your name? > ")
print(f"Nice to meet you, {name}!")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"The sum of {a} and {b} is {a + b}.")

messages = [
    "Keep coding, you're doing great! 💪",
    "Every commit counts 🚀",
    "Bugs are just hidden lessons 🐞",
    "You're one push closer to mastery ⭐"
]

print(random.choice(messages))
