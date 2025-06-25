fruits = ['apple', 'banana', 'cherry']
print(fruits)

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

colors = ['red', 'green']
colors.extend(['blue', 'yellow'])
print(colors)


animals = ['cat', 'dog', 'rabbit']
animals.insert(1, 'hamster')
print(animals)


cities = ['London', 'Paris', 'New York']
cities.remove('Paris')
print(cities)


languages = ['Python', 'Java', 'C++']
removed = languages.pop(0)
print(languages, removed)

scores = [88, 75, 92, 60]
scores.sort()
print(scores)

letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)


nums = [1,2,2,3,2,0,3,5,3,3,2,2,4]
count_2 = nums.count(2)
print(count_2)

original = [5, 10, 15]
copy_list = original.copy()
print(copy_list)