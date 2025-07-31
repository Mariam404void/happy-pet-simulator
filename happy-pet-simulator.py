pet_name = "Mochi"
happiness = 0

while True:
    print(f"\nWhat would you like to do with {pet_name}?")
    print("1. Feed")
    print("2. Pet")
    print("3. Check happiness")
    print("4. Exit")

    choice = input("Choose number between 1-4: ")

    if choice == "1":
        if happiness < 10:
            happiness += 1
            print(f"You fed {pet_name}.")
        else:
            print(f"{pet_name} is already full.")



    elif choice == "3":
        if happiness >= 8:
            mood = "Very happy"
        elif happiness >= 5:
            mood = "Doing okay"
        else:
            mood = "Feeling a little down"

        print(f"{pet_name}'s happiness: {happiness}/10 — {mood}")

    elif choice == "4":
        print(f"Goodbye! {pet_name} will miss you.")
        break

    else:
        print("Invalid choice. Please try again.")
