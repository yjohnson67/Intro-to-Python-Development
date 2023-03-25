#The "with" syntax helps you so you don't have to worry about if you close the file or not, as it does it for you.
with open("books.text") as book_file:

    #Go through each line in the file
    for line in book_file:

        #The "strip" function gets rid of any added white space at the beginning and ending of each line
        book = line.strip()

        #Print the code out onto the screen.  
        print(book)
