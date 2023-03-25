import csv

# Read the data from the CSV file
data_list = []
with open("life-expectancy.csv") as file:
    reader = csv.reader(file)
    headers = next(reader) # skip the first row (headers)
    for line in reader:
        country = line[0]
        country_code = line[1]
        year = int(line[2].strip())
        life_expectancy = float(line[3].strip())
        data_list.append([country, country_code, year, life_expectancy])

# Find the overall max and min life expectancy
overall_max_le = 0
overall_min_le = float('inf')
max_le_country = ''
min_le_country = ''
max_le_year = 0
min_le_year = 0
for line in data_list:
    if line[3] > overall_max_le:
        overall_max_le = line[3]
        max_le_country = line[0]
        max_le_year = line[2]
    if line[3] < overall_min_le:
        overall_min_le = line[3]
        min_le_country = line[0]
        min_le_year = line[2]

# Print the overall max and min life expectancy
print("The overall max life expectancy is: {:.3f} from {} in {}".format(overall_max_le, max_le_country, max_le_year))
print("The overall min life expectancy is: {:.3f} from {} in {}".format(overall_min_le, min_le_country, min_le_year))

# Find the life expectancy for the year of interest
year_examined = input('Enter the year of interest: ')
ages = []
for line in data_list:
    if line[2] == int(year_examined):
        ages.append(line[3])

# Calculate the average life expectancy
average_age = sum(ages) / len(ages)

# Find the max and min life expectancy for the year of interest
max_le = 0
min_le = float('inf')
max_le_country = ''
min_le_country = ''
for line in data_list:
    if line[2] == int(year_examined):
        if line[3] > max_le:
            max_le = line[3]
            max_le_country = line[0]
        if line[3] < min_le:
            min_le = line[3]
            min_le_country = line[0]

# Print the average, max and min life expectancy for the year of interest
print("For the year {}:".format(year_examined))
print("The average life expectancy across all countries was {:.2f}".format(average_age))
print("The max life expectancy was in {} with {:.2f}".format(max_le_country, max_le))
print("The min life expectancy was in {} with {:.3f}".format(min_le_country, min_le))

# Find the largest drop for the year of interest
largest_drop = 0
drop_country = ''
drop_year = 0
for i in range(1, len(data_list)):
    if data_list[i][0] == data_list[i-1][0]:
        drop = data_list[i-1][3] - data_list[i][3]
        if drop > largest_drop:
            largest_drop = drop
            drop_country = data_list[i][0]
            drop_year = data_list[i][2]

print("The largest drop was {:.3f} in {} from {} to {}".format(largest_drop, drop_country, drop_year, drop_year + 1))

country_of_interest = input("Enter the country of interest: ")
ages = []
for line in data_list:
    if line[0] == country_of_interest.title():
        ages.append(line[3])

average_age = sum(ages) / len(ages)
max_le = max(ages)
min_le = min(ages)

print("For {}:".format(country_of_interest))
print("The average life expectancy was {:.3f}".format(average_age))
print("The max life expectancy was {:.3f}".format(max_le))
print("The min life expectancy was {:.3f}".format(min_le))

