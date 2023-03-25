list_number = []
number = -1

while number != 0:
    number = int(input("Enter number:"))

    if number !=0:
        list_number.append(number)
#The list of numbers the user has inputed

#Step 1: Find the sum or total:
sum = 0

for number in list_number:
    sum += number

print(f"The sum is: {sum}")

#Step 2: Find the average:
#The sum we just computed can be used to find the average:
count = len(list_number)
average = sum / count

print(f"The average is: {average}")

#Step 3: Find the highest number
#Code is walking through the numbers again keeping track of the best so far or the highest number.
list_number.sort()
print(f"The largest number is: ", list_number[-1])
        

###Stretch Challenges###

#Stretch Challenge #1: Find the smallest positive number:
#We need to start with a large number
smallest_so_far = 9999999999999
#To be most accurate, instead of starting with a big number like the one above, looping through the list until
#we find a positive number and ust that as the smallest_so_far becasue it is simpler to see and understand, but 
#think about this....what if the list doesn't have any positive numbers?  What if it didn't have any less than the
#biggest number picked?  These owuld create problems that would be solved by the approach mentioned.  
for number in list_number:
    if number > 0 and number < smallest_so_far:
        smallest_so_far = number

print(f"The smallest positive number is: {smallest_so_far}")

#stretch challenge #2: Sorting the list:
sorted_list = sorted(list_number)
print("The sorted list is: ")
for number in sorted_list:
    print(number)
