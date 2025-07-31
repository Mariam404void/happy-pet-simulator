while True:
    choice = input("Enter 1 to feed, 2 to pet, 3 to check if happy, 4 to exit: ").strip()

    if choice == "1":
        print("You fed Mochi.")

    elif choice == "2":
        print("You pet Mochi.")

    elif choice == "3":
        print("Mochi is happy!")

    elif choice == "4":
        print("Goodbye! Mochi will miss you")
        break

    else:
        print("Invalid choice.")