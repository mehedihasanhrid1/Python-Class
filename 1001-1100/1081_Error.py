while True:
    try:
        n = int(input("Enter a number: "))
        if n%2 == 0:
            print("Even!")
        else:
            print("Odd!")
    except ValueError:
        print("Error!")