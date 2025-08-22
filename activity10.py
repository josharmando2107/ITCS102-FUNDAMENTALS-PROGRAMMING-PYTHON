#comment

name = input("Input your name ---> ")
isStudent = input("Are you student (Yes / No) --> ")
fare = eval(input("bayad --> "))

if isStudent.lower() == "yes":
            discount = fare * .2
            new_fare = fare - discount 
            print("His", name, "student discount is ", discount, "Discounted fare is ", new_fare)
else:
            print("Sorry ", name," you are not eligible for student discount")