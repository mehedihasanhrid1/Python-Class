lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

for n in range(lower,upper+1):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n, end=' ')

