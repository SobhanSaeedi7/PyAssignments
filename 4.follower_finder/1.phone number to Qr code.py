import qrcode

print("HI")
print("Let`s make a Qr code for your phone number")

name = input("Enter your name : ")
phone_number = input("Enter your phone number : ")

qr = qrcode.make(name+"]["+phone_number)

qr.save("my number.png")