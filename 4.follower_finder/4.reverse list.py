print("Hi")

list = []

while True :
    number = input("Enter a number to add to list or write 'exit' : ")
    if number.isnumeric() :
        list.append(number)
    elif number == "exit" :
        break
    else :
        print("Just enter a number or write'exit'")

reversed_list=list[::-1]
print("Reversed list : ",reversed_list)