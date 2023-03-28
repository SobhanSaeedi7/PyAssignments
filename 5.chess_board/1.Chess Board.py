#Making Chess Board
lenth = int(input("Enter lenth of chess board : "))
width = int(input("Enter width of chess board : "))

for i in range (lenth):
    for s in range(width):
        if s%2 == 0 :
            print("#", end="")
        else :
            print("*", end="")
    print(" ")