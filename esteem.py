print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
print("This program will show you ten statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the statements by responding with one of these four letters:")
print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.\n")

score = 0

questions = [
    "I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all."
]

for i, question in enumerate(questions, start=1):
    answer = input(f"{i}. {question}\nEnter D, d, a, or A: ")
    if answer == "D":
        score += 0
    elif answer == "d":
        score += 1
    elif answer == "a":
        score += 2
    elif answer == "A":
        score += 3

print(f"\nYour score is {score}.")
if score < 15:
    print("A score below 15 may indicate problematic low self-esteem.")