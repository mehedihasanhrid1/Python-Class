marks = [15, 20, 18, 22, 25, 30, 28, 19, 21, 24,15,18,30,18]

print("Original list:", marks)

print("Total length of the list:", len(marks))

print(type(marks))

print("First element of the list:", marks[0])
print("Sixth element of the list:", marks[5])
print("Last element of the list:", marks[-1])

print("Range:", marks[2:9])

fruits = ["apple", "banana", "cherry", "date", "strawberry"]

fruits.insert(3,'orange')

fruits.remove("banana")
print(fruits)