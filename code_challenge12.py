


#diamond

print("\t\t *", end=" ")
for i in range(1, 3, 1):
    print("             ", end=" ")
    for y in range(3, i, -1):
        print(" ", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()


for i in range(3, 1, -1):
    print("             ", end=" ")
    for y in range(3, i, -1):
        print(" ", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()

#smallest triangle

print("\t\t *", end=" ")
for i in range(1, 7, 1):
    print("       ", end=" ")
    for y in range(6, i, -1):
        print(" ", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()

#smaller triangle
print("\t\t *", end=" ")
for i in range(1, 9, 1):
    print("   ", end=" ")
    for y in range(8, i, -1):
        print(" ", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()
#triangle

print("\t\t *", end=" ")
for i in range(1, 11, 1):
    for y in range(10, i, -1):
        print(" ", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, 1):
        print("*", end=" ")
    print()
#paa
for i in range(1, 5, 1):
    print("\t     ", end=" ")
    for y in range(5, i, -1):
        print("*", end=" ")
    for x in range(1, i, 1):
        print("*", end=" ")
    for z in range(1, i, -1):
        print("*", end=" ")
    print()