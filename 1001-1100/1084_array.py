import array

arr = array.array('i', [25, 60, 52, 25, 24, 46, 25, 15, 19])

print("Array contents:", list(arr))

while True:
    print("\nArray Operations Menu:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        val = int(input("Enter value to insert: "))
        arr.append(val)
        print(f"{val} inserted.")
        print("Array contents:", list(arr))
    elif choice == '2':
        val = int(input("Enter value to delete: "))
        if val in arr:
            arr.remove(val)
            print(f"{val} deleted.")
            print("Array contents:", list(arr))
        else:
            print(f"{val} not found in array.")
    elif choice == '3':
        val = int(input("Enter value to search: "))
        if val in arr:
            print(f"{val} found at index {arr.index(val)}.")
        else:
            print(f"{val} not found in array.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
