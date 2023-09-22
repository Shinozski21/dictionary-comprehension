# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {names: grade for (names, grade) in students_score.items() if grade > 80}
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#Looping through dicitonaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
#print(student_df)

#Loop through a data frame

# for (key, value) in student_df.items():
#     print(value)

#Loop through rows of a data frame

for (index, row) in student_df.iterrows():
    print(row.student)
