print("LCM Finder")
number1 = int(input("enter first number : "))
number2 = int(input("Enter second number : "))

C1 = 1
C2 = 1

while True :
    M1 = C1 * number1
    M2 = C2 * number2
    if M1 > M2 :
        C2 += 1
    elif M2 > M1 :
        C1 += 1
    else : 
        break

print("LCM = ",M1)
print(number1,"*",C1,"=",M1)
print(number2,"*",C2,"=",M2)