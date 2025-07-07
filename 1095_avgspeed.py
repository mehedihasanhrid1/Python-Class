a = 10
b = 20
c = 30

avg = (a + b + c) / 3
print(f"Average speed: {avg} km/h")

if a < avg:
    print("Cyclist 1 is riding slower than the average speed.")
if b < avg:
    print("Cyclist 2 is riding slower than the average speed.")
if c < avg:
    print("Cyclist 3 is riding slower than the average speed.")
if not (a < avg or b < avg or c < avg):
    print("No cyclist is riding slower than the average speed.")