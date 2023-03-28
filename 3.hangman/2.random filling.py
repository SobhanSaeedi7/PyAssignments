import random

list=[]
number_of_numbers = int(input("Please enter length of the list : "))
length_of_list = 0


enter = input("Press enter to start")

while length_of_list < number_of_numbers :
    number = (random.randint(1, 10*number_of_numbers)) 
    if not number in list :
        list.append(number)
        length_of_list += 1 


print("list:",list)   