from arc_data import studentData


def avg_percentage(subjects):
    male_total = 0    
    male_count = 0
    female_total = 0
    female_count = 0


    for student in subjects:
        percent = sum(student["marks"]) / len(student["marks"])
        if student["isMale"]:
            male_total += percent
            male_count += 1
        else:
            female_total += percent
            female_count += 1

    
    if male_count > 0:
        perOfMale = male_total / male_count
    else:
        perOfMale = 0

    if female_count > 0:
        perOfFemale = female_total / female_count 
    else:
        perOfFemale = 0


    return perOfMale, perOfFemale

# call function
perOfMale, perOfFemale = avg_percentage(studentData)
print("Male Avg % :", round(perOfMale, 2))
print("Female Avg % :", round(perOfFemale, 2))
