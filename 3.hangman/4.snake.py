print("Hi🖐")
print("Let`s make your snake🐍")

len_snake = int(input("Choose and enter length of snake"))

for i in range(len_snake) :
    if i % 2 == 0 :
        print("*", end="")
    else :
        print("#",end="")
