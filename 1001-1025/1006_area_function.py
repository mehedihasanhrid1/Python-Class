# def area_of_square(side):
#     area = side ** 2
#     return area

# print("-------------------------------------")
# print("-----------Area Calculator-----------")
# print("-------------------------------------")

# print("Choose a shape to calculate the area:")
# print("1. Square")
# print("2. Rectangle")
# print("3. Circle")
# print("4. Triangle")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     side = float(input("Enter the length of the side of the square: "))
#     area = area_of_square(side)
#     print(f"The area of the square is: {area: 0.2f}")


def area_of_square(side):
    area = side ** 2
    return area
def area_of_rectangle(length,width):
    area = length * width
    return area
def area_of_circle(radius):
    return 3.14 * radius ** 2
def area_of_triangle(base,height):
    return 0.5 * base * height

print("--------------------------------------------------")
print("area calculator")
print("--------------------------------------------------")

print("Chooose a shape to calculate the area:")
print("1. Square")
print("2.Rectangle")
print("3.Circle")
print("4.Triangle")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    side = float(input("Enter the side length of the square: "))
    area = area_of_square(side)
    print(f"The area of the square is: {area}")
elif choice == 2:
    length = float(input("Enter The length of the rectangle: "))
    width = float(input("Enter The width of the rectangle: "))
    area = area_of_rectangle(length,width)
    print(f"The area of the rectangle is : {area:.2f}")
elif choice == 3:
    radius = float("Enter The Radius Of The Circle:")
    area = area_of_circle(radius)
    print(f"The area of the circle is: {area:.2f}")
elif choice == 4:
    base = float(input("Enter The Base of the triangle:"))
    height = float(input("Enter The height of the triangle:"))
    area = area_of_triangle(base, height)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Invalid Choice.Please Try Again.")
