from datetime import datetime

def show_welcome_message():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        "==============================\n"
        " 🚀 Your code is now on GitHub! 🎉 \n"
        "==============================\n"
        f"Time: {now}\n"
        "Keep coding and growing 💪😎\n"
    )
    return message

if __name__ == "__main__":
    print(show_welcome_message())
