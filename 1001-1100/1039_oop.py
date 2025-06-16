class StringOperations:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def to_lower(self):
        return self.text.lower()

    def reverse(self):
        return self.text[::-1]

    def count_words(self):
        return len(self.text.split())

if __name__ == "__main__":
    a = "Madam In Eden, I'm Adam"
    s = StringOperations(a)
    print("Original:", s.text)
    print("Uppercase:", s.to_upper())
    print("Lowercase:", s.to_lower())
    print("Reversed:", s.reverse())
    print("Word count:", s.count_words())