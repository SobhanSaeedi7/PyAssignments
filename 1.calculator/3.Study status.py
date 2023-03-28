print("Hi")
print("After you enter your final exam scores , I`ll check them and then I`ll tell you, your study status")

name = str(input("please enter your name:"))
family = str(input("please enter your family name:"))
a = float(input("enter first score:"))
b = float(input("enter second score:"))
c = float(input("enter third score:"))

avg = (a + b + c) / 3
print(name,family,"your scors average is:",avg)

if avg >= 17:
        print("And your study status is:Great")
elif 17 > avg >= 12:
        print("And your study status is:Normal")
elif 12 > avg:
        print("And your study status is:Fail")
