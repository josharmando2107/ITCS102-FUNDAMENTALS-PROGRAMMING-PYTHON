#create a program that accepts float
#determine temperature
#negative infinity freezing cold temperature
#1 to 20 cold
#21 to 30 lukewarm
#31 to 40 warm 
#41 to 50 hot
#51 and above boiling hot


temp = eval(input("Enter temperature --> "))

if temp >= 1 and temp  <= 20:
           print("temperature outside is cold")
elif temp >= 21 and temp <= 30:
           print("temperature outside is lukewarm")
elif temp >= 31 and temp <= 40:
           print("temperature outside is warm")
elif temp >= 41 and temp <=50:
           print("temperature outside is hot")
elif temp >= 51:
           print("temperature outside is boiling hot")
elif temp <=0:
           print("temperature outside is freezing cold")

else:
           print("invalid temperature")