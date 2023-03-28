print("Hi")

factorial = 1
counter = 0

number = int(input("Enter a number to see it`s factorial or not : "))

while True :
    counter += 1
    factorial *= counter

    if factorial == number :
        print("Number ",number," is factorial✅")
        break
    elif factorial > number :
        print("Number ",number," isn`t factorial❌")
        break