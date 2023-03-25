#defining the fuction to display the output correctly
def display_regular(message):
    print(message)

def display_uppercase(message):
    print(message.upper())

def display_lowercase(message):
    print(message.lower())

message = input("What is your message? ")

#calling the function to display the output
display_regular(message)
display_uppercase(message)
display_lowercase(message)