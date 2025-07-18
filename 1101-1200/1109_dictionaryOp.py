student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "courses": ["Math", "Physics"],
    "is_active": True
}

print("Original Dictionary:", student)

print("Name:", student["name"])

student["email"] = "alice@example.com"
print("After adding email:", student)


student["grade"] = "A+"
print("After updating grade:", student)


removed_age = student.pop("age")
print("Removed age:", removed_age)
print("After removing age:", student)

print("Phone:", student.get("phone", "Not Provided"))
print("Email:", student.get("email", "Not Provided"))


print("Keys:", list(student.keys()))


print("Values:", list(student.values()))


print("Items:", list(student.items()))


print("Has 'courses' key?", "courses" in student)

print("Looping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

student.clear()
print("After clearing:", student)