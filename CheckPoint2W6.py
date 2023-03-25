people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
#Recognize the age as well as the youngest_person in the list
min_age = float("inf")
youngest_person = ""

#Go through each person in the list and gifure out which one is the youngest.  
for person in people:
    name, age = person.split(" ")
    age = int(age)
    if age < min_age:
        min_age = age
        youngest_person = name

print("The youngest person is", youngest_person)