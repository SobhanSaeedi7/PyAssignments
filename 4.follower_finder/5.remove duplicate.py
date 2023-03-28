print("Hello")
print("Enter your list number to remove duplicate numbers")

list=[]

while True :
    numbers = input("Enter a number or write 'exit' to exit : ")

    if numbers == "exit" :
            break
    elif numbers.isnumeric() :
        if numbers not in list :
            list.append(numbers)
    else :
        print("Please just enter number or write 'exit' ")

print("List after removing duplicate numbers : ",list)