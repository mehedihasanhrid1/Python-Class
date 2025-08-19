print("-"*30)
print("Times Table Generator".center(30))
print("-"*30)

n = int(input("Enter the table index: "))
print("-"*30)

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    
print("-"*30)   
    