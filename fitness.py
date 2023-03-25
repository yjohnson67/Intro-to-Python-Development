from datetime import datetime


def main():
    print("Welcome to the fitness tracker!")
    # Prompt the user for input.
    gender = input("Please enter your gender? ")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    weight_st = float(input("Enter your weight in British stones: "))
    height_in = float(input("Enter your height in U.S. inches: "))
    
    # Call the necessary functions to compute the results.
    age = compute_age(birthdate_str)
    weight_kg = kg_from_stone(weight_st)
    height_cm = m_from_ft_in(0, height_in)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Display the results to the user.
    print("Your age is: {} years".format(age))
    print("Your weight is: {:.2f} kg".format(weight_kg))
    print("Your height is: {:.2f} m".format(height_cm))
    print("Your BMI is: {:.2f}".format(bmi))
    print("Your BMR is: {:.2f} kcal/day".format(bmr))


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years


def kg_from_stone(stones):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return stones * 6.35029


def m_from_ft_in(feet, inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return feet * 30.48 + inches * 2.54


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return weight / (height / 100) ** 2


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        gender: a person's gender ("M" or "F").
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "M":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.upper() == "F":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Must be M or F")
if __name__ == "__main__":
    main()