import random

def wordle_game():
    #welcome
    print("Welcome to the game of words!")
    # List of words to choose from
    word_list = ["mosiah", "jacob", "adam", "noah", "mary"]
    # Choose a random word from the list
    word = random.choice(word_list)
    # Convert the word to a list of characters
    word_letters = list(word)
    # Create a list of underscores the same length as the word
    word_guess = ["_" for letter in word_letters]
    # Keep track of the player's incorrect guesses
    incorrect_guesses = []
    # Keep track of the number of hints used
    hints_used = 0
    guess_used = 0
    while "_" in word_guess:
        # Print the current word_guess
        print(" ".join(word_guess))
        # Get the player's guess
        guess = input("Guess a letter or the whole word: ").lower()
        guess_used +=1
        # Check if the player's guess is a single letter or the whole word
        if len(guess) == 1:
            # Check if the letter is in the word
            if guess in word_letters:
                # Replace the underscores with the correct letter
                for i in range(len(word_letters)):
                    if word_letters[i] == guess:
                        word_guess[i] = guess
                print("Great, you guessed a correct letter!")
            else:
                # Add the incorrect letter to the list of incorrect guesses
                incorrect_guesses.append(guess)
                print("Incorrect! The letter is not in the word.")
                hint = input("Do you want a hint? y/n ").lower()
                if hint == "y":
                    hints_used += 1
                    print("The word contains the letter: ", random.choice(word_letters))
                elif hint =="n":
                    print()
                else:
                    print("Invaid response!  Please answer with a y or n next time.")
        elif len(guess) == len(word):
            if guess == word:
                # Player guessed the word correctly
                word_guess = list(word)
            else:
                # Player guessed the wrong word
                incorrect_guesses.append(guess)
                print("Incorrect! That is not the word.")
                hint = input("Do you want a hint? y/n ").lower()
                if hint == "y":
                    hints_used += 1
                    print("The word contains the letter: ", random.choice(word_letters))
        else:
            print("Invalid input. Please enter a single letter or the whole word.")
       
        if "_" not in word_guess:
            print("You win! The word was", word)
    if "_" not in word_guess:
        print("You used", hints_used, "hints.")
        print("You used", guess_used, "guesses.")

wordle_game()