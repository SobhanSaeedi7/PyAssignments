print("Check the list is in order or it`s not")

list=[]
order = True

while True:
    number = input("enter one number to add to list or write something to exit : ")
    if number.isnumeric() :
        list.append(number)
        if len(list) > 2 :
            if list[len(list)-1] > list[len(list)-2] :
                order = False

    else :
        break

print("list : ",list)
if order:
    print("List is in order👍")
else :
    print("List isn`t in order👎")