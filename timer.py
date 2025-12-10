import time

def countdown(seconds: int):
    print(f"⏳ Countdown started for {seconds} seconds...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_view = f"{mins:02d}:{secs:02d}"
        print(f"\rTime left: {timer_view}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n✅ Time is up!")

def stopwatch():
    print("▶ Stopwatch started. Press Ctrl + C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            timer_view = f"{mins:02d}:{secs:02d}"
            print(f"\rElapsed: {timer_view}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹ Stopwatch stopped.")

def main():
    print("⏱ Simple Timer")
    print("1 — Countdown")
    print("2 — Stopwatch")

    choice = input("Choose mode (1 or 2): ")

    if choice == "1":
        try:
            seconds = int(input("Enter seconds for countdown: "))
            if seconds <= 0:
                print("❌ Time must be positive.")
            else:
                countdown(seconds)
        except ValueError:
            print("❌ Please enter a valid number.")
    elif choice == "2":
        stopwatch()
    else:
        print("❌ Unknown option.")

if __name__ == "__main__":
    main()
