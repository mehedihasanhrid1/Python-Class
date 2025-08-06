class StringOperator:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def to_lower(self):
        return self.text.lower()

    def reverse(self):
        return self.text[::-1]

    def is_palindrome(self):
        return self.text == self.text[::-1]

    def count_vowels(self):
        return sum(1 for char in self.text.lower() if char in 'aeiou')

    def replace_word(self, old, new):
        return self.text.replace(old, new)

    def find_word(self, word):
        return self.text.find(word)

    def word_count(self):
        return len(self.text.split())

    def remove_whitespace(self):
        return self.text.strip()

    def capitalize_words(self):
        return self.text.title()

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    operator = StringOperator(sentence)

    print("\nString Operations:")
    print("1. Uppercase:", operator.to_upper())
    print("2. Lowercase:", operator.to_lower())
    print("3. Reversed:", operator.reverse())
    print("4. Is Palindrome:", operator.is_palindrome())
    print("5. Vowel Count:", operator.count_vowels())
    print("6. Replace 'a' with '@':", operator.replace_word('a', '@'))
    print("7. Find 'the':", operator.find_word('the'))
    print("8. Word Count:", operator.word_count())
    print("9. Trimmed:", operator.remove_whitespace())
    print("10. Capitalize Words:", operator.capitalize_words())
