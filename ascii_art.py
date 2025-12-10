def show_art():
    art = r"""
      /\_/\  
     ( o.o ) 
      > ^ <
    """
    print(art)

def show_menu():
    print("🎨 ASCII Art Viewer")
    print("1 — Cat 🐱")
    print("2 — Heart ❤️")
    print("3 — Rocket 🚀")
    print("4 — Exit")

def show_heart():
    heart = r"""
     _  _    
   _( \/ )_  
  (_     _) 
    (_/\/_)  
    """
    print(heart)

def show_rocket():
    rocket = r"""
       /\
      /  \
     |    |
     |🚀🚀|
      \  /
       \/
    """
    print(rocket)

def main():
    while True:
        show_menu()
        choice = input("\nChoose option (1-4): ")

        if choice == "1":
            show_art()
        elif choice == "2":
            show_heart()
        elif choice == "3":
            show_rocket()
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Unknown option.")

if __name__ == "__main__":
    main()
