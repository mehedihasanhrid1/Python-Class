w = float(input("Enter your weight in KG: "))
h = float(input("Enter your height in meter: "))

bmi = w / h ** 2

print("Your BMI is:",round(bmi,2))

if bmi < 18.5:
    print("You are underweight. Gain some weight.")
elif 18.5 <= bmi <= 24.9:
    print("You are normal in weight. Keep it up!")
elif 25 <= bmi <= 29.9:
    print("You are overweight. Lose some weight.")
elif 30 <= bmi <= 34.9:
    print("You are obese. Loosing weight is emergency for you.")
else:
    print("You are extremly obese. Visit the doctor as soon as possible.")