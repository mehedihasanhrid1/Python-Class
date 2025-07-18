class StringOperations:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def to_lower(self):
        return self.text.lower()

    def reverse(self):
        return self.text[::-1]

    def is_palindrome(self):
        cleaned = ''.join(filter(str.isalnum, self.text)).lower()
        return cleaned == cleaned[::-1]

    def count_vowels(self):
        return sum(1 for c in self.text.lower() if c in 'aeiou')

    def word_count(self):
        return len(self.text.split())

    def replace(self, old, new):
        return self.text.replace(old, new)

    def remove_spaces(self):
        return self.text.replace(' ', '')

    def get_unique_characters(self):
        return set(self.text)

    def __str__(self):
        return self.text

def main():
    print("Welcome to String Operations Project!")
    user_input = input("Enter a string: ")
    s = StringOperations(user_input)

    while True:
        print("\nChoose an operation:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Reverse string")
        print("4. Check palindrome")
        print("5. Count vowels")
        print("6. Word count")
        print("7. Replace substring")
        print("8. Remove spaces")
        print("9. Get unique characters")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("UPPERCASE:", s.to_upper())
        elif choice == '2':
            print("lowercase:", s.to_lower())
        elif choice == '3':
            print("Reversed:", s.reverse())
        elif choice == '4':
            print("Is palindrome?", s.is_palindrome())
        elif choice == '5':
            print("Vowel count:", s.count_vowels())
        elif choice == '6':
            print("Word count:", s.word_count())
        elif choice == '7':
            old = input("Enter substring to replace: ")
            new = input("Enter new substring: ")
            print("Result:", s.replace(old, new))
        elif choice == '8':
            print("Without spaces:", s.remove_spaces())
        elif choice == '9':
            print("Unique characters:", s.get_unique_characters())
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()