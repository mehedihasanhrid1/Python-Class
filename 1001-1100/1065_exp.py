try:
    x = 25 / 0
except ZeroDivisionError as e:
    print("Error: ",e)
    
try:
    y = int("abc")
except ValueError as e:
    print("Error: ",e)

try:
    data = [15, 22, 37]
    z = data[5]
except IndexError as e:
   print("Error: ",e)
    
try:
    n = 105
    n.append(6)
except AttributeError as e:
    print("Error: ",e)

try:
    print(result)
except NameError as e:
    print("Error: ",e)
    