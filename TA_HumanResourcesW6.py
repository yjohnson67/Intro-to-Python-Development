with open("hr_system.txt") as employee_file:

    for line in employee_file:
        parts = line.split(" ")

        name = parts[0]
        name_id = parts[1]
        title = parts [2]
        salary = float(parts[3])

        annual_amount = salary / 12
        

        if title.lower() == "engineer":
            annual_amount += 1000

        print(f"{name} {name_id} {title} {salary} - ${annual_amount:.2f}")