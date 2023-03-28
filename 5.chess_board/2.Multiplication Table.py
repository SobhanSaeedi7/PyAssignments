#Show Multiplication Table
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

for i in range (second_number+1):
    for s in range(first_number+1):
        if i == 0 and s == 0 :
            print("⇲ ", end="\t")
        elif i == 0 or s == 0 :
            print(i+s, end="\t")
        else:
          print((i) * (s), end="\t")
    print(" ")