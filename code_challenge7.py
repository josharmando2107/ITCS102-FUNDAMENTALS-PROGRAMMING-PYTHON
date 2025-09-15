pre = 0
for x in range(10):
    inp = eval(input("Input 10 numbers from 1-10:\t"))
    d = inp % 2
    if d == 1:
        pre += inp
print("The total summation of the odd numbers input are",pre)
