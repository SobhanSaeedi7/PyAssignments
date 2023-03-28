import instaloader
import getpass

print("Hi")
print("Here I help you finding your new instagram follower")
#1:Check old followers
file_using = open("Followers.txt", "r")
old_followers = []
for line in file_using :
    old_followers.append(line.strip())

file_using.close()

#2:log in
user_name = input("Enter your username ; ")
while True :
    enter_password = input("Do you want to enter your password secret (s) or not (n) ?")
    if enter_password == "n" :
        user_password = input("Enter your password ; ")
        break
    elif enter_password == "s" :
        user_password = getpass.getpass("Enter your password ; ")
        break
    else :
        print("Please enter 's' or 'n' ")

log_in = instaloader.Instaloader()
log_in.login(user_name, user_password)
profile = instaloader.Profile.from_username(log_in.context, user_name)

#3:Check followers
new_followers = []
for follwer in profile.get_followees() :
    new_followers.append(follwer)

#4:Find new follower and unfollowers
for new_follower in new_followers :
    if new_follower not in old_followers :
        print("New followers from last update : ",new_follower)
for old_follower in old_followers :
    if old_follower not in new_followers :
        print("Unfollowers from last update : ",old_follower)

#5:Update followers.txt
file_using2 = open("followers.txt", "w")
for new_follower2 in new_followers :
    file_using2.write(new_follower2 + "/n")
file_using2.close()
