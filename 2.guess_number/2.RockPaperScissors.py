import random

print("HI🤗")
print("THIS time let`s play Rock Paper Scissors😍")

user_score = 0
camputer_score = 0

while user_score < 3 and camputer_score < 3 :

    camputer_choose = random.randint(1, 3)

    if camputer_choose == 1 :
        camputer_choose = "R"
    elif camputer_choose == 2 :
        camputer_choose = "P"
    elif camputer_choose == 3 :
        camputer_choose = "S"


    user_choose = input ("What`s your choose?R🧱,P📜 or S✂ : ")

    

    if camputer_choose == user_choose :
        print("Your choose is same as my choose")
    elif (camputer_choose == "R" and user_choose == "P") or (camputer_choose == "P" and user_choose == "S") or (camputer_choose == "S" and user_choose == "R") :
        user_score = user_score + 1
        print("OWW 😕")
        print("👤 Your score: ",user_score)
        print("🤖 My score: ",camputer_score)
    elif (camputer_choose == "R" and user_choose == "S") or (camputer_choose == "P" and user_choose == "R") or (camputer_choose == "S" and user_choose == "P") :
        camputer_score = camputer_score + 1
        print("Yeah 🤩")
        print("👤 Your score: ",user_score)
        print("🤖 My score: ",camputer_score)
    else :
        print("Please enter correct choose(R🧱,P📜 or S✂)")

print("👤 Your score: ",user_score)
print("🤖 My score: ",camputer_score)
if user_score == 3 :
    print("You win 😖🎉")
elif camputer_score == 3 :
    print("You lose 🤣✌")