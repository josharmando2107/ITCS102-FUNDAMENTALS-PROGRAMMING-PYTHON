# FINALS_PROJECT.py

name = input("Enter your name -->>")


# actcc = input("What category do you want to access ACTIVITIES or CODE CHALLENGES? (A/C) -->> ").lower()

while True:
    actcc = input("What category do you want to access ACTIVITIES or CODE CHALLENGES? (A/C), press (X) to exit -->> ").lower()
    if actcc =='a':
        print("You have selected ACTIVITIES")
        print ("Loading Activities...")

        while True:
            print("============================================")
            print(f"WELCOME TO THE FINAL PROJECT PROGRAM {name}")
            print("============================================")


            selected_activity = input("select activity nuber\n1. Activity 1\t11. Activity 11\t 21. Activity 21\n2. Activity 2\t12. Activity 12\t 22. Activity 22\n3. Activity 3\t13. Activity 13\t 23. Activity 23\n4. Activity 4\t14. Activity 14\t 24. Activity 24\n5. Activity 5\t15. Activity 15\t 25. Activity 25\n6. Activity 6\t16. Activity 16\t 26. Activity 26\n7. Activity 7\t17. Activity 17\t 27. Activity 27\n8. Activity 8\t18. Activity 18\t 28. Activity 28\n9. Activity 9\t19. Activity 19\n10. Activity 10\t20. Activity 20\n0. exit program\n\nEnter activity number: ")

            if selected_activity == "1":
                while True:
                    print("========================")
                    print("ACTIVITY 1 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('"Print()" function is used to display output to the console.')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity1 import activity1
                        activity1()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "2":
                while True:
                    print("========================")
                    print("ACTIVITY 2 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('The input() function in Python is a built-in function used to read\n a line of text (a string) from the user, usually via a console or terminal,\n and return that string to the program..')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activty2 import activty2
                        activty2()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "3":
                while True:
                    print("========================")
                    print("ACTIVITY 3 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" the escape sequences in Python are special characters that are \nused to represent certain whitespace or non-printable characters within strings. \nThey are preceded by a backslash (\\) and have specific meanings.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity3 import activity3
                        activity3()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "4":
                while True:
                    print("========================")
                    print("ACTIVITY 4 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("The len() function in Python is a built-in function that returns \nthe number of items \nin an object. When used with strings, it returns the number of \ncharacters in the string.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity4 import activity4
                        activity4()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "5":
                while True:
                    print("========================")
                    print("ACTIVITY 5 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("In Python, the type() function is a built-in function that returns\n the type of an object or variable.It helps you determine the data type of a given value,\n such as whether it's an integer, string, list, etc.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity5 import activity5
                        activity5()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "6":
                while True:
                    print("========================")
                    print("ACTIVITY 6 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, arithmetic operations are performed using standard\n mathematical operators such as\n + (addition), - (subtraction), * (multiplication), / (division), ** (exponentiation), % (modulus), and // (floor division).\nThese operators allow you to perform calculations on numerical values.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity6 import activity6
                        activity6()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "7":
                while True:
                    print("========================")
                    print("ACTIVITY 7 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, augmented assignment operators are shorthand notations that combine\n a basic arithmetic operation with assignment. They allow you to update the value \nof a variable\n by performing an operation on its current value and assigning the result back to the same variable.\nCommon augmented assignment operators include +=, -=, *=, /=, %=, //=, and **=.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity7 import activity7
                        activity7()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "8":
                while True:
                    print("========================")
                    print("ACTIVITY 8 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, comparison operators are used to compare two values \nor expressions and return a Boolean result (True or False). \nThese operators include > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), == (equal to), and != (not equal to). \nThey are commonly used in conditional statements and loops to control the flow of a program based on certain conditions.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity8 import activity8
                        activity8()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "9":
                while True:
                    print("========================")
                    print("ACTIVITY 9 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, logical operators are used to combine multiple Boolean expressions and return a single Boolean result. \nThe three main logical operators are 'and', 'or', and 'not'.\nThe 'and' operator returns True if both operands are True, the 'or' operator returns True if at least one operand is True, \nand the 'not' operator negates the Boolean value of its operand.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity9 import activity9
                        activity9()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "10":
                while True:
                    print("========================")
                    print("ACTIVITY 10 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, conditional statements are used to perform different actions based on whether a certain condition is true or false. \nThe most common conditional statements are 'if', 'elif', and 'else'.\nThe 'if' statement checks a condition and executes a block of code if the condition is true.\nThe 'elif' statement allows you to check multiple conditions sequentially, executing the corresponding block of code for the first true condition.\nThe 'else' statement provides a default block of code to execute if none of the previous conditions are true.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity10 import activity10
                        activity10()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "11":
                while True:
                    print("========================")
                    print("ACTIVITY 11 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" In Python, conditional statements are used to perform different actions based on whether a certain condition is true or false. \nThe most common conditional statements are 'if', 'elif', and 'else'.\nThe 'if' statement checks a condition and executes a block of code if the condition is true.\nThe 'elif' statement allows you to check multiple conditions sequentially, executing the corresponding block of code for the first true condition.\nThe 'else' statement provides a default block of code to execute if none of the previous conditions are true.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity11 import activity11
                        activity11()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "12":
                while True:
                    print("========================")
                    print("ACTIVITY 12 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('the for loop in Python is a control flow statement that allows you \nto iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. \nIt enables you to execute a block of code repeatedly for each item in the sequence, \nmaking it easy to perform repetitive tasks or process collections of data.')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity12 import activity12
                        activity12()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "13":
                while True:
                    print("========================")
                    print("ACTIVITY 13 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("using for loop, ask user to input 10 numbers after input, get the summation of all the numbers")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity13 import activity13
                        activity13()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "14":
                while True:
                    print("========================")
                    print("ACTIVITY 14 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("ascending order and descending order using for loop")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity14 import activity14
                        activity14()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "15":
                while True:
                    print("========================")
                    print("ACTIVITY 15 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("input 10 numbers, get the summation of all the odd numbers")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity15 import activity15
                        activity15()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "16":
                while True:
                    print("========================")
                    print("ACTIVITY 16 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" using loop print 1-10 horizontaly")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity16 import activity16
                        activity16()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "17":
                while True:
                    print("========================")
                    print("ACTIVITY 17 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" print 1-10 horizontally for 10 rows")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity17 import activity17
                        activity17()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "18":
                while True:
                    print("========================")
                    print("ACTIVITY 18 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" print pattern of numbers in increasing order")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity18 import activity18
                        activity18()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "19":
                while True:
                    print("========================")
                    print("ACTIVITY 19 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" print pattern of asterisks in increasing order")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity19 import activity19
                        activity19()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "20":
                while True:
                    print("========================")
                    print("ACTIVITY 20 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" print pattern of asterisks and numbers in increasing and decreasing order")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity20 import activity20
                        activity20()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "21":
                while True:
                    print("========================")
                    print("ACTIVITY 21 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" print pattern of numbers in decreasing order")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity21 import activity21
                        activity21()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "22":
                while True:
                    print("========================")
                    print("ACTIVITY 22 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Importing functions or modules to achieve specific tasks or functionalities in your program.\n in this case is importing randoms and user trying\n to guess the number generated by the random module')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity22 import activity22
                        activity22()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "23":
                while True:
                    print("========================")
                    print("ACTIVITY 23 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("creating list and appending items to it based on user input until a certain condition is met.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity23 import activity23
                        activity23()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
        
            elif selected_activity == "24":
                while True:
                    print("========================")
                    print("ACTIVITY 24 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("creating custom functions to perform specific tasks, such as greeting users and calculating the sum of numbers in a list.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity24 import activity24
                        activity24()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "25":
                while True:
                    print("========================")
                    print("ACTIVITY 25 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" creating a file compiler that allows users to select and run different activities from a menu-driven interface.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity25 import activity25
                        activity25()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "26":
                while True:
                    print("========================")
                    print("ACTIVITY 26 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print(" Selecting items from list by mentioning their index positions")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity26 import activity26
                        activity26()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "27":
                while True:
                    print("========================")
                    print("ACTIVITY 27 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("Creating a dictionary that can store data inputed and print out the stored data.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity27 import activity27
                        activity27()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_activity == "28":
                while True:
                    print("========================")
                    print("ACTIVITY 28 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->>")

                    if do == "1":
                        print("==============================================================")
                        print("This is the command for the pygame snake you can install py game\n and paste this commands.")
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from activity28 import activity28
                        activity28()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_activity == "0":
                print("Exiting program...")
                break
    elif actcc =='c':
        print("You have selected CODE CHALLENGES")
        print ("Loading Code Challenges...")
        while True:
            print("========================")
            print("CODE CHALLENGES MENU")
            print("========================")
            selected_cc = input("Select a Code Challenge Number\n 1. Code Challenge 1\t 11. Code Challenge 11\n 2. Code Challenge 2\t 12. Code Challenge 12\n 3. Code Challenge 3\t 13. Code Challenge 13\n 4. Code Challenge 4\t 14. Code Challenge 14\n 5. Code Challenge 5\t 15. Code Challenge 15\n 6. Code Challenge 6\t 16. Code Challenge 16\n 7. Code Challenge 7\n 8. Code Challenge 8\n 9. Code Challenge 9\n 10. Code Challenge 10\n 0. Exit program\n\n Enter code challenge number-->> ")

            if selected_cc == "1":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 1 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Printing  name inside of diamond')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge1 import code_challenge1
                        code_challenge1()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
                
            elif selected_cc == "2":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 2 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Counting every place value in deposited ammount')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge2 import code_challenge2
                        code_challenge2()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "3":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 3 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Crating username and password system')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge3 import code_challenge3
                        code_challenge3()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
                
            elif selected_cc == "4":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 4 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Determining if a number is even or odd')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge4 import code_challenge4
                        code_challenge4()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "5":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 5 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('generating manga recommender based on user input')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge5 import code_challenge5
                        code_challenge5()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "6":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 6 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('generating factorial of a user inputed number')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge6 import code_challenge6
                        code_challenge6()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "7":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 7 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Enter 10 numbers, determine if odd or even, and find the summation of odd numbers')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge7 import code_challenge7
                        code_challenge7()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "8":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 8 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('#Ask the user to input a number.Use a for loop to print the \nmultiplication table from for that number.\nFormat each line clearly (e.g., 5 x 1 = 5).')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge8 import code_challenge8
                        code_challenge8()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "9":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 9 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Simulate a simple countdown timer using a for loop that counts \nfrom a user-specified number down to 1,then prints "Liftoff! ".')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge9 import code_challenge9
                        code_challenge9()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "10":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 10 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('making a pyramind using for loop')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge10 import code_challenge10
                        code_challenge10()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
               
            elif selected_cc == "11":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 11 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('making a Diamond using for loop')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge11 import code_challenge11
                        code_challenge11()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "12":
               while True:
                    print("========================")
                    print("CODE CHALLENGE 12 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('making acending numerical pyramid using for loop')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge12 import code_challenge12
                        code_challenge12()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "13":
                 while True:
                    print("========================")
                    print("CODE CHALLENGE 13 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('making a X-mas Tree with a diamond top using for loop')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge13 import code_challenge13
                        code_challenge13()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
               
            elif selected_cc == "14":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 14 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('Making an odd number compiler that sums all odd numbers inputed by user until user inputs 0 to terminate the loop')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge14 import code_challenge14
                        code_challenge14()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break

            elif selected_cc == "15":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 15 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('adding items to a list until user inputs "done" to terminate the loop and show all items in the list')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge15 import code_challenge15
                        code_challenge15()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
            
            elif selected_cc == "16":
                while True:
                    print("========================")
                    print("CODE CHALLENGE 16 MENU")
                    print("========================")
                    do = input("Choose an option: \n1. Definition \n2. Run Program \n3. Back to options \n\nEnter option number-->> ")

                    if do == "1":
                        print("==============================================================")
                        print('making a data storage system using JSON to store and retrieve data\n and also print the data and able to edit and delete data')
                        print("==============================================================")
                    elif do == "2":
                        print("++++++++++++++++++++++++++++++++++++++")
                        from code_challenge16 import code_challenge16
                        code_challenge16()
                        print("++++++++++++++++++++++++++++++++++++++")
                    elif do == "3":
                        break
                        

            elif selected_cc == "0":
                print("Exiting program...")
                break
    elif actcc =='x':
        print("Exiting program... Thank you for using the program!")
        
        exit()
