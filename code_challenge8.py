#prints the number enter by the user
print("MULTIPLICCATION TABLE MAKER")

num = eval(input("Enter a number: "))
print(f"\nMultiplication table for {num}:")

for x in range(1, 11):
    result = num * x
    print(f"{num} * {x} = {result}")