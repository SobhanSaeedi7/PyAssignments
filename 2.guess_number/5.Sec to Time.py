print("Sec to Time converter")

seconds = int(input("enter second : "))

hour = seconds//3600
minute = (seconds-hour*3600)//60
second =  (seconds-hour*3600-minute*60)

print(seconds,"⏩",hour,":",minute,":",second)