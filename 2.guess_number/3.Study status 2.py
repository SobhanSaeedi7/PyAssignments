print("Hi")
print("After you enter your exam scores , I`ll check them and then I`ll tell you, your study status")

name = str(input("please enter your name:"))
family = str(input("please enter your family name:"))
score_number = 1
score = int(input("enter first score:  "))

while True :
    next_scores = input("enter next score or write exit : ")
    if next_scores != "exit" :
        score_number = score_number+1
        score = score + int(next_scores)
    else : 
        break
    

avg = score/score_number
print(name,family,"your scores average : ",avg)

if avg >= 17:
        print("And your study status is:Great")
elif 17 > avg >= 12:
        print("And your study status is:Normal")
elif 12 > avg:
        print("And your study status is:Fail")
