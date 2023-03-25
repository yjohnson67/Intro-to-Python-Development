# Initialize a variable to keep track of the largest number of chapters

volume_of_choice = input("Which volume of scripture would you like to learn about? ")

largest_chapters = -1
largest_book = ""

# Open the file and read it line by line
with open("books_and_chapters.txt") as file:
    for line in file:
        #split the line based on the ":"
        parts = line.split(":")

        #read in the book and strip off any whitespace at the beginning and ending
        book = parts[0].strip()

        #Getting the number of chapters as an integer
        chapters = int(parts[1])

        #Getting the volume of scripture and strip off any whitespace at the beginning and ending
        scripture = parts[2].strip()

        #Checking to see if this belongs to the user's chosen volume:
        if scripture.lower() == volume_of_choice.lower():
            #Only display and check for the most inside the body of the if statement.  This will be a way of
            #limiting the infomration to the user's chosen volume.
    
            print(f"Scritpure: {scripture}, Book: {book}, Chapters: {chapters}")

        #Checking to see if this book has the most chapters so far
        if chapters > largest_chapters:
            #This best book is the newest one!
            largest_chapters = chapters #The max chapters in now this book
            largest_book = book # Rembering the name of the book

#Printing after the loop is done
print(f"The book with the most chapters is: {largest_book}")
print(f"It has {largest_chapters} chapters.")