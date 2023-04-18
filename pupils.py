import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(my_list):
    """Print each element of a list on a separate line."""
    for element in my_list:
        print(element)
    print()

def main():
    try:
        #Call the read_compound_list function to read the pupils.csv file into a list named students_list.
        students_list = read_compound_list("pupils.csv")

        # Write a lambda function that will extract the birthdate from a student.
        get_birthdate = lambda student: student[BIRTHDATE_INDEX]

        # Write a lambda function that will extract the given name from a student.
        get_given_name = lambda student: student[GIVEN_NAME_INDEX]

        # Write a lambda function that will extract the birth month and day from a student.
        get_birth_month_day = lambda student: student[BIRTHDATE_INDEX][5:]

        # Sort the students_list by birthdate from oldest to youngest.
        students_list = sorted(students_list, key=get_birthdate)

        # Print the students_list by calling the print_list function.
        print("Ordered from Oldest to Youngest")
        print_list(students_list)

        # Sort the students_list by given name.
        students_list = sorted(students_list, key=get_given_name)

        # Print the students_list sorted by given name.
        print("Ordered by Given Name")
        print_list(students_list)

        # Sort the students_list by birth month and day.
        students_list = sorted(students_list, key=get_birth_month_day)

        # Print the students_list sorted by birth month and day.
        print("Ordered by Birth Month and Day")
        print_list(students_list)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

if __name__ == "__main__":
    main()      
