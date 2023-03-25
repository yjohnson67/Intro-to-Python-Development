import random
#The main() function calls several other functions to perform the following tasks:

#prints a list of numbers
#generates and appends a random number to the list of numbers
#generates and appends three random numbers to the list of numbers
#generates a list of six random words from a given list of words

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers: {numbers}")
    
    append_random_numbers(numbers)
    print(f"numbers: {numbers}")
    
    append_random_numbers(numbers, 3)
    print(f"numbers: {numbers}")

    words = ["join" , "love", "smile", "love", "cloud", "head"] 
    random_words = generate_random_words(words, 6)
    print(f"words: {random_words}")
    
#The append_random_numbers() function takes a list of numbers and a quantity as arguments and 
# generates random numbers using the random.uniform() function. The quantity parameter defaults 
# to 1 if not provided. The generated numbers are then rounded to one decimal place and appended 
# to the numbers list.
def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_number = round(random_number, 1)
        numbers_list.append(rounded_number)

#The generate_random_words() function takes a list of words and a quantity as arguments and uses 
# the random.sample() function to generate a list of random words from the given list. The quantity 
# parameter defaults to 1 if not provided. If the requested quantity is greater than the length of 
# the list, the function returns the entire list.
def generate_random_words(words_list, quantity=1):
    if quantity > len(words_list):
        return words_list
    else:
        return random.sample(words_list, quantity)   

#The if __name__ == '__main__': block ensures that the main() function is only called if the script 
# is being run directly, rather than being imported as a module.
if __name__ == '__main__':
    main()