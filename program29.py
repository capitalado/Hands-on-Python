#List of dictionaries and filter function to extract
#students with a grade greater than or equal to 95

students = [{'name': 'Pablo', 'age': 23, 'grade': 90 },
            {'name': 'Gupta', 'age': 40 , 'grade': 70},
            {'name': 'Emmett', 'age': 52, 'grade': 50},
            {'name': 'Kakaa', 'age': 102 , 'grade': 96}]

# Filter students with a grade greater than or equal to 95
filtered_students = list(filter(lambda student: student['grade'] >= 95, students))

# Print filtered students
for student in filtered_students:
    print(student)