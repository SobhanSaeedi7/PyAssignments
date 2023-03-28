import random

print("Hellpppp!!!🥵")
print("There is a word and you have 7 chance to find it and save my life😬")

word_bank = ["room","car","phone","case","pen","sofa","work","school","wallpaper","workspace","football","download","hardest one"]

life_len = 7
word = random.choice(word_bank)
word = word.lower()
true_chars=[]
false_chars=[]
X = True


for i in range(len(word)):

        if word[i]in " ":
            print(" ", end="")
        else:
            print("_", end="")
            


while life_len > 0 :

    user_char = input("enter your guess : ").lower()

    if len(user_char) == 1:

        if user_char in true_chars or user_char in false_chars :
            print("Are you play joke on my life!!!Be careful my life is in danger don`t writ repetitious😡")

        else :
            if user_char in word :
                true_chars.append(user_char)
                print("yeah right 😓")
    
            else :
                false_chars.append(user_char)
                print("Oh no you was wrong😱")
                life_len -= 1
        X = False
        for i in range(len(word)):
            if word[i] == " ":
                print(" ", end="")
            elif word[i] in true_chars :
                print(word[i], end="")
            else:
                print("_", end="")
                X = True

        print("fault chars :", end="")
        for i in range(len(false_chars)):
            print(false_chars[i], end="-")
        print("")

        if X == False:
            print("Thanks so much,,You saved my life😍")
            break
    else :
        print("I know my life is important for you but you can just enter one character😐")
if life_len == 0 :
    print("Dead ☠")