QUESTIONS = [
    {
        "question": "Какой язык ты сейчас тренируешь? (a) Python  (b) Java  (c) C++",
        "answer": "a"
    },
    {
        "question": "GitHub — это: (a) текстовый редактор  (b) хостинг репозиториев  (c) игра",
        "answer": "b"
    },
    {
        "question": "Какой символ используют для комментариев в Python? (a) //  (b) <!-- -->  (c) #",
        "answer": "c"
    },
    {
        "question": "Какой командой отправляют коммиты на GitHub? (a) git send  (b) git push  (c) git upload",
        "answer": "b"
    },
]

def run_quiz():
    print("🧠 Simple Quiz Game")
    score = 0

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {i}:")
        print(q["question"])
        user_answer = input("Your answer (a/b/c): ").strip().lower()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n📊 Results:")
    print(f"You answered correctly on {score} out of {len(QUESTIONS)} questions.")
    if score == len(QUESTIONS):
        print("🔥 Perfect! Well done!")
    elif score >= len(QUESTIONS) // 2:
        print("👍 Not bad, keep going!")
    else:
        print("💪 More practice and you'll get better!")

if __name__ == "__main__":
    run_quiz()
