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
