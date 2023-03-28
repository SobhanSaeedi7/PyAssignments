print("enter a number to get Fibonacci numbers")

number = int(input("enter number : "))
a = 1
b = 0


for i in range(number) :
    result = a + b
    a = b
    b = result
    print(result)