running = True

while running:
    n = input("Enter a number or 'exit' to quit: ")
    if n.lower() == 'exit':
        running = False
        print("Exiting the program.")
    else:
        n = int(n)
        if n % 2 == 0:
            print(f"{n} is even.")
        else:   
            print(f"{n} is odd.")