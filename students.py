import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the headers
        students_dict = {}
        for row in reader:
            inumber = row[0].replace('-', '')  # remove dashes from I-Number
            name = row[1]
            students_dict[inumber] = name
        return students_dict

def is_valid_inumber(inumber):
    """Check if the given string is a valid I-Number.

    Parameters:
        inumber: the string to check.
    Return: True if the string is a valid I-Number, False otherwise.
    """
    if not all(char.isdigit() or char == '-' for char in inumber):
        print("Invalid I-Number")
        return False
    inumber_digits = inumber.replace('-', '')
    if len(inumber_digits) < 9:
        print("Invalid I-Number: too few digits")
        return False
    elif len(inumber_digits) > 9:
        print("Invalid I-Number: too many digits")
        return False
    return True

def main():
    filename = 'students.csv'
    students_dict = read_dictionary(filename)
    inumber = input("Please enter an I-Number: ")
    if is_valid_inumber(inumber):
        name = students_dict.get(inumber.replace('-', ''))
        if name:
            print(f"The student with I-Number {inumber} is {name}.")
        else:
            print("No such student")

if __name__ == '__main__':
    main()