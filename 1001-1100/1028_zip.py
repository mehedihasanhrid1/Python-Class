fruits = ['Mango', 'Apple', 'Banana', 'Orange']
prices= [120, 80, 60, 100]

new_data = {fruits:prices for fruits, prices in zip(fruits, prices)}
print(new_data)