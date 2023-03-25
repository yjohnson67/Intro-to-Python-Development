friends = []

name_friend = None
while name_friend!= "end":
    name_friend = input("Type the name of a friend: ")
    
    if name_friend != "end": 
        friends.append(name_friend)

print()
print("Your friends are: ")
for friend in friends:
    print(friend)    