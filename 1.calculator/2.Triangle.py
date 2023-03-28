print("HI")
print("I`ll tell you if your triangle is drawable or not")


a = float(input("please enter length of the first side"))
b = float(input("please enter length of the second side"))
c = float(input("please enter length of the third side"))

if b + c > a and a + c > b and a + b > c:
        print("it`s drawable")
else:
        print("it isn`t drawble")