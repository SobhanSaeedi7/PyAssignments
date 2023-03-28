import random

print("Hi👋")
print("I`m Dice🎲")
print("You roll me one time and if I roll 6 you can roll one time more🙌")



while True :
    dice = random.randint(1, 6)
    if dice == 6 :
        print("Ohh I`m 6 you can roll me again☝🖐")
    else :
        print("I`m not 6 now you lost your chance🙍") 
        break
