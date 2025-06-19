def main():
    while True:
        print("\nMenu:")
        print("1. Print even numbers up to N")
        print("2. Skip vowels in a word")
        print("3. Placeholder option (pass)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            n = int(input("Enter N: "))
            print("Even numbers up to", n)
            for i in range(1, n+1):
                if i % 2 != 0:
                    continue 
                print(i, end=' ')
            print()
        elif choice == '2':
            word = input("Enter a word: ")
            print("Word without vowels:", end=' ')
            for ch in word:
                if ch.lower() in 'aeiou':
                    continue  
                print(ch, end='')
            print()
        elif choice == '3':
            pass 
            print("This feature is coming soon!")
        elif choice == '4':
            print("Exiting program.")
            break  
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()