def calculate_average(grade1, grade2):
    return (grade1 + grade2) / 2

students = []

number_students = input("How many students do you want to add? (between 2 and 7)")

while not number_students.isdigit() or int(number_students) < 2 or int(number_students) > 7:
    number_students = input("Invalid number! Please enter a number (between 2 and 7): ")

number_students = int(number_students)

for i in range(number_students):
    print(f"--------STUDENT {i + 1}--------")

    name = input("Enter the student's name:")
    while not name.replace(" ", "").isalpha():
        name = input("Invalid name! Please enter letters only: ")

    grade1 = input("Enter the first grade (0 to 10): ")

    while not grade1.replace(".", "").isdigit() or float(grade1) < 0 or float(grade1) > 10:
        grade1 = input("Invalid grade! Please enter the first grade (0 to 10): ")

    grade1 = float(grade1)

    grade2 = input("Enter the second grade (0 to 10): ")

    while not grade2.replace(".", "").isdigit() or float(grade2) < 0 or float(grade2) > 10:
        grade2 = input("Invalid grade! Please enter the second grade (0 to 10): ")

    grade2 = float(grade2)

    average = calculate_average(grade1, grade2)

    student = {
        "name": name,
        "grade1": grade1,
        "grade2": grade2,
        "average": average
    }

    students.append(student)


print("======== STUDENT AVERAGE ========")

for student in students:
    print("-----------------------------")
    print(f"Name: {student['name']}")
    print(f"Grade 1: {student['grade1']:.2f}")
    print(f"Grade 2: {student['grade2']:.2f}")
    print(f"Average: {student['average']:.2f}")
    print("------------------------------")

sum_averages = 0
for student in students:
    sum_averages += student['average']

class_average = sum_averages / len(students)

number_students = len(students)

highest = students[0]
lowest = students[0]

for student in students:
    if student['average'] > highest['average']:
        highest = student
    if student['average'] < lowest['average']:
        lowest = student

print("======== CLASS SUMMARY ========")
print(f"The class average is: {class_average:.2f}")
print(f"The number of students is: {number_students}")
print(f"Highest average: {highest['name']} with {highest['average']:.2f}")
print(f"Lowest average: {lowest['name']} with {lowest['average']:.2f}")