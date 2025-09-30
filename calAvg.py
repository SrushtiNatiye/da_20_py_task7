from arc_data import studentData, subjectNames


#num_students = len(studentData)
#num_subjects = len(subjectNames)

#totals_marks_for_each = [0] * num_subjects

#for studs in studentData:
#   for i in range(num_subjects):
#        totals[i] += student["marks"][i]

#averages = [totals[i] / num_students for i in range(num_subjects)]

# print result
#for i in range(num_subjects):
#    print(subjectNames[i], ":", round(averages[i], 2))





# total students
total_students = len(studentData)

# calculate average for each subject
for i in range(len(subjectNames)):
    total = 0
    for student in studentData:
        total += student["marks"][i]
    avg = total / total_students
    print(subjectNames[i], ":", round(avg, 2))
