unit =  int(input("Enter the unit of electricity consumed: "))

if unit < 50:
    bill = unit * 2.60
    tax = 25
elif unit <= 100:
    bill = (50*2.60) + ((unit - 50) * 3.25)
    tax = 35
elif unit <= 200:
    bill = (50*2.60) + (50*3.25) + ((unit - 100) * 5.26)
    tax = 45
else:
    bill = (50*2.60) + (50*3.25) + (100*5.26) + ((unit - 200) * 8.45)
    tax = 75

total = bill + tax

print("Electricity Bill:", total)
