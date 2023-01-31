import random
keepPlaying = "y"
num = 100
while keepPlaying == "y":
    magicNum = random.randint(1, num)
    guess = True

    num = input("Welcome to the number guessing game, what is the max number you would like to be able to guess up to? ")
while True:
    try:
        num = int(num)
        if num > 1:
            break
        else:
            print("Enter a number greater than 1")
    except ValueError:
        print("This is not a valid number. Please enter a valid number")

    magicNum = random.randint(1, num)
    guess = True

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {num}: "))
        except ValueError:
            print("This is not a valid number.  Please enter a valid number. ")       
        if guess < magicNum:
            print("Too low!  Try again. ")
        elif guess > magicNum:
            print("Too high!  Try again. ")
        else:    
            print("Congratulations!!!  You guessed it!")
            play_again = input("Do you want to play again? y/n ")
            if play_again.lower() == "y":
                continue
            else:
                print("Thanks for playing!")
                break