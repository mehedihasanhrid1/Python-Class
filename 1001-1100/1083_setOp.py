def display_menu():
    print("\nSet Operations Menu:")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (A - B)")
    print("4. Difference (B - A)")
    print("5. Symmetric Difference")
    print("6. Exit")

def main():
    print("Welcome to the Set Operations Project!")
    set_a = {'apple', 'banana', 'orange'}
    set_b = {'banana', 'date', 'orange'}

    print("Set A:", set_a)
    print("Set B:", set_b)

    while True:
        display_menu()
        choice = input("Choose an operation (1-6): ")

        if choice == '1':
            print(set_a.union(set_b))
        elif choice == '2':
            print(set_a.intersection(set_b))
        elif choice == '3':
            print(set_a.difference(set_b))
        elif choice == '4':
            print(set_b.difference(set_a))
        elif choice == '5':
            print(set_a.symmetric_difference(set_b))
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
