print("Time to Sec converter")

hour = int(input("enter hour : "))
minute = int(input("enter minute : "))
second = int(input("enter second : "))

result = (hour*60 + minute)*60 + second

print(hour,":",minute,":",second,"⏩",result)