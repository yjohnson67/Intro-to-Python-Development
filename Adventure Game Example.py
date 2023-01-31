name = input("Let's get aquainted, what is your name? ").capitalize()
print(f"Hello {name}!  Welcome to this adventure, good luck!")
start = input("Would you like to take a risk and play? (yes/no) ") 
if start == "yes":
    print("Great! Let's get on with the adventure!")
    setting = input("Would you like to go to the jungle or the desert? ").lower()
    
    

    if setting == "jungle":  
        print("Welcome to the might Amazon rainforest!  Your tour guide told you to wait...")
        response = input("but he has been gone for quit some time now...Follow him or wait here? ")
        if response == "follow":
            choice = input("You know he headed towards the river, there is a canoe nearby. Would you like to follow him by walking or canoe (walk/canoe?)  ")
            if choice == "walk":
                print("As soon as you walk into the woods a huge python snake finds you and crushes you with it's strength...you die! ")
                print("Game Over!  You PERISH!")
                quit()
            elif choice == "canoe":
                 print("As soon as you get in the canoe a huge wave washes you overboard and leaches attack and drain your blood!")
                 print("Game Over!  You PERISH!")  
                 quit()    
        if response == "wait":
            print("You wait another 10 minutes, and he still isn't back!")
            choice = input("Keep waiting or follow him? ")
            if choice == "wait":
                print("He finally comes back!  He said the Jungle is lame and the tour is over!")
                quit()
            elif choice == "follow":
                print("You follow in the direction you saw him go and you get lost and are lost in the jungle forever running from \ncreatures to save your life!")
                quit()
   
    if setting == "desert":
        print("Welcome to the mighty Sahara Desert!  Your tour guide told you to wait here...")
        response = input("But he has been gone for a while now...Follow him or wait here? ")
        if response == "follow":
            choice = input("You saw him head towards the Pyramids, there's a camel nearby.  Would you like to follow him by \nwalking or riding the camel? (please respond with one of these options walk/camel) ")
            if choice == "walk":
                print("You get lost and stuck in the desert due to a sand storm.  You have to be rescued!  You Lose!")
                quit()
            elif choice == "camel":
                print("You are in luck my friend, because the camel you are riding is a very smart camel and leads you straight \nto the treasure and CONGRATULATIONS!!! Now you are a billionaire!")
            quit()
        if response == "wait":
            print("You wait another ten minutes and he still isn't back!")
            choice = input("Keep waiting or follow him? ")
            if choice == "wait":
                print("The guide finally comes back and says the Desert is way too hot and the tour has been cancelled!")
                quit()
            elif choice == "follow":
                print("You start following in the direction the guide went, but then a huge sand storm comes along, you get lost and \n have to be rescued.  You LOSE!")
    else:
        print("Invalid response!  You lose!")
        quit()
elif start == "no":
    print("Okay you PERISH, good work....")
else:
    print("Not a valid response, you LOSE!")