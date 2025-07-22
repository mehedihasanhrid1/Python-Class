words = input("Enter a string to check the occurence: ")
letter = input("Enter a letter to find the count: ")

count = 0

for i in words:
    if i == letter:
        count = count + 1
        
print(f"The letter '{letter}' occurs {count} times in the string.")

