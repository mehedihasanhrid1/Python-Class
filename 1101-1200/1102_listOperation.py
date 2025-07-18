numbers = [10, 20, 30, 40, 50]
fruits = ['apple', 'banana', 'cherry']

numbers.append(60)
print("After append:", numbers)

fruits.insert(1, 'orange')
print("After insert:", fruits)

numbers.remove(30)
print("After remove:", numbers)

last_fruit = fruits.pop()
print("After pop:", fruits)
print("Last fruit popped:", last_fruit)

banana_index = fruits.index('banana')
print("Index of banana:", banana_index)

numbers.sort()
print("After sort:", numbers)

fruits.reverse()
print("After reverse:", fruits)

count_20 = numbers.count(20)
print("Count of 20 in numbers:", count_20)

numbers.extend(fruits)
print("After extend:", numbers)

fruits_copy = fruits.copy()
print("Fruits copy:", fruits_copy)
