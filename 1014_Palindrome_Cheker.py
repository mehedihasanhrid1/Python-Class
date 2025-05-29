word = str(input("Enter a word: "))
n = ''
for w in word:
    n = w + n
    
if n == word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
    