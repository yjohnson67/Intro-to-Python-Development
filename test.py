import csv

YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        filename = input("Please enter the filename that contains NHTSA data: ")
        with open(filename, "rt") as infile:
            perc_reduc = get_float("Enter the percentage reduction of texting while driving [0, 100]: ", 0, 100)
            print()
            print(f"With a {perc_reduc}% reduction in using a cell phone while driving, the following number of injuries and deaths could have been prevented in the USA.")
            print()
            print("Year, Injuries, Deaths")
            reader = csv.reader(infile)
            next(reader)

            for row in reader:
                year = row[YEAR_COLUMN]
                injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)
                print(year, injur, fatal, sep=", ")

    except (FileNotFoundError, PermissionError) as error:
        print(f"Error: {error}. Please choose a different file.")

    except ValueError as val_err:
        print(f"Error: {val_err}. Please enter a valid input.")

    except (csv.Error, KeyError) as error:
        print(f"Error: {error}.")

    except ZeroDivisionError as zero_div_err:
        print(f"Error: {zero_div_err}. The 'Fatal Crashes' or 'Cell Phone Use' column contains 0.")


def get_float(prompt, lower_bound, upper_bound):
    number = None
    while number == None:
        try:
            number = float(input(prompt))
           if number < lower_bound:
                raise ValueError(f"Error: {number} is too low." \
                        f" Please enter a different number.")
            elif number > upper_bound:
                print(f"Error: {number} is too high." \
                        f" Please enter a different number.")
                number = None
        except ValueError as val_err:
            print(val_err)
    print()
    return number


def estimate_reduction(row, behavior_key, perc_reduc):
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


if __name__ == "__main__":
    main()