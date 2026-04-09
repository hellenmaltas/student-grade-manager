def calculate_average(grade1, grade2):
    return (grade1 + grade2) / 2

students = []

number_students = int(input("How many students do you want add? (From 2 to 7)"))

while number_students < 2 or number_students > 7:
    number_students = int(input("Invalid number! Please enter a number (From 2 and 7."))

for i in range (number_students):
    print(f"--------STUDENT {i + 1}--------")

    name = (input("Enter the student's name:"))

    grade1 = float(input("Enter the first grade(0 to 10): "))
    while grade1 < 0 or grade1 > 10:
        grade1 = float(input("Invalid grade! Please enter the first grade (From 0 to 10): "))

    grade2 = float(input("Enter the second grade(0 to 10): "))
    while grade2 < 0 or grade2 > 10:
        grade2 = float(input("nvalid grade! Please enter the second grade (From 0 to 10): "))

    average = (calculate_average(grade1, grade2))

    student ={
        "name" : name,
        "grade1" : grade1,
        "grade2" : grade2,
        "average" : average
    }

    students.append(student)


print("======== STUDENT AVERAGE ========")

for student in students:
    print("-----------------------------")
    print(f"Name: {student['name']}")
    print(f"Grade 1: {student['grade1']}")
    print(f"Grade 2: {student['grade2']}")
    print(f"Average: {student['average']}")
    print("------------------------------")

sum_averages = 0
for student in students:
    sum_averages += student['average']

class_average = sum_averages / len(students)

number_students = len(students)

highest = students[0]  # Começa com o primeiro aluno
lowest = students[0]

for student in students:
    if student['average'] > highest['average']:
        highest = student
    if student['average'] < lowest['average']:
        lowest = student

print("======== CLASS SUMMARY ========")
print(f"The class average is: {class_average:.2f}")
print(f"The number of students is: {number_students}")
print(f"The student with the highest average was {highest['name']} with {highest['average']:.2f}")
print(f"The student with the lowest average was {lowest['name']} with {lowest['average']:.2f}")