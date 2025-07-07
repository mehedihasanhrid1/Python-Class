def add_lists(list1, list2):
    return list(map(lambda x: x[0] + x[1], zip(list1, list2)))

def main():
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]

    if len(list1) != len(list2):
        print("Lists must be of the same length. Exiting.")
        exit(1)

    result = add_lists(list1, list2)
    print("Result of adding corresponding elements:")
    print(result)

if __name__ == "__main__":
    main()
