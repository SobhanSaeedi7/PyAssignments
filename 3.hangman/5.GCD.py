print("GCD finder")
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

D1 = []
D2 = []
GCD = 1

for i in range(1, number1):
    if (number1/i).is_integer():
        D1.append(i)

for i in range(1, number2) :
    if (number2/i).is_integer():
        D2.append(i)
        if i in D1 :
            GCD = i

print("GCD = ",GCD)