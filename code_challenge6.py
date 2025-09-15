print("FACTORIAL PROGRAM")

num = eval(input("Input a number --->  "))

result = 1
for x in range(num, 0 , -1):
    #print(x)
    result *= x

print("factorial is ",result)     