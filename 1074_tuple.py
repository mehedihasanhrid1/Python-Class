def create_tuple():
    return tuple(input("Enter elements separated by space: ").split())

def display_tuple(t):
    print("Tuple:", t)

def length_tuple(t):
    print("Length:", len(t))

def access_element(t):
    idx = int(input("Enter index to access: "))
    print("Element at index", idx, ":", t[idx])

def count_element(t):
    elem = input("Enter element to count: ")
    print(f"Count of '{elem}':", t.count(elem))

def index_element(t):
    elem = input("Enter element to find index: ")
    print(f"Index of '{elem}':", t.index(elem))

def concatenate_tuple(t):
    t2 = tuple(input("Enter elements for second tuple: ").split())
    print("Concatenated Tuple:", t + t2)

def repeat_tuple(t):
    n = int(input("Enter number of repetitions: "))
    print("Repeated Tuple:", t * n)

def min_max_tuple(t):
    try:
        t_num = tuple(map(float, t))
        print("Min:", min(t_num), "Max:", max(t_num))
    except ValueError:
        print("Tuple contains non-numeric values.")

def tuple_to_list(t):
    print("Converted to list:", list(t))

def main():
    print("Tuple Operations Project")
    t = create_tuple()
    while True:
        print("\nChoose an operation:")
        print("1. Display Tuple")
        print("2. Length of Tuple")
        print("3. Access Element by Index")
        print("4. Count Occurrence of Element")
        print("5. Find Index of Element")
        print("6. Concatenate with Another Tuple")
        print("7. Repeat Tuple")
        print("8. Find Min and Max (numeric)")
        print("9. Convert Tuple to List")
        print("10. Exit")
        choice = input("Enter choice (1-10): ")
        if choice == '1':
            display_tuple(t)
        elif choice == '2':
            length_tuple(t)
        elif choice == '3':
            access_element(t)
        elif choice == '4':
            count_element(t)
        elif choice == '5':
            index_element(t)
        elif choice == '6':
            concatenate_tuple(t)
        elif choice == '7':
            repeat_tuple(t)
        elif choice == '8':
            min_max_tuple(t)
        elif choice == '9':
            tuple_to_list(t)
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()