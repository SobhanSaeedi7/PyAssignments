import random

print("HI👋")
print("Let`s play a game😃")
print("I choose one number from 1 to 100 and you have 20 chance to guess it😎")

camputer_number = random.randint(1,100)
number_of_guess = 0

while number_of_guess < 20:
        guessed_number =int(input("enter the number you guessed:  "))
        if camputer_number > guessed_number :
                number_of_guess = number_of_guess+1
                print("Go Up⏫")
        elif guessed_number < guessed_number :
                number_of_guess = number_of_guess+1
                print("Go Down⏬")
        else :
                number_of_guess = number_of_guess+1
                break
if number_of_guess < 20 :
        print("You win😒🎉")
        print("number of guess :  ",number_of_guess)
else :
        print("You lose💪😛")
        