try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

try:
    y = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    data = [15, 22, 37]
    z = data[5]
except IndexError as e:
    print(f"IndexError: {e}")

try:
    d = {"a": 1}
    v = d["b"]
except KeyError as e:
    print(f"KeyError: {e}")

try:
    s = "abc" + 5
except TypeError as e:
    print(f"TypeError: {e}")

try:
    with open("data.txt") as f:
        f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

try:
    n = 5
    n.append(6)
except AttributeError as e:
    print(f"AttributeError: {e}")

try:
    print(result)
except NameError as e:
    print(f"NameError: {e}")
    
