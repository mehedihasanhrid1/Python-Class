a = int(input("Enter your amount: "))

print("Denomaition:")

note1000 = a // 1000
print("1000 TAKA Note:",note1000)
a = a % 1000

note500 = a // 500
print("500 TAKA Note:",note500)
a = a % 500

note200 = a // 200
print("200 TAKA Note:",note200)
a = a % 200

note100 = a // 100
print("100 TAKA Note:",note100)
a = a % 100
