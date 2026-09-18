def village():
    while True:
        print("\n" + "=" * 45)
        print("ELDORIA VILLAGE")
        print("=" * 45)

        print("1. Leave village")

        choice = input("Choose: ")
        if choice == "1":
            break
        else:
            print("Invalid choice.")
