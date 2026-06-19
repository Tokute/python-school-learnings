grade_file = open("Studgrade.txt", "w+")

grade_file.write("Ned,92,93,94,95\n")
grade_file.write("Angelina,95,96,97,97\n")
grade_file.write("Kenn,92,91,90,99")

grade_file.close()

grade_file = open("Studgrade.txt", "r")

student_grades = []

for data in grade_file:
    student_grades.append(data.rstrip().split(','))

#print(student_grades)
grade_file.close()

computed_grades = open("Studentreport.txt", "w+")

def calculate_grade(student=None):
    total = 0
    if student is None:
        student = []
    else:
        student=student
        
    student_name = student[0]

    for i in range(1, (len(student)), 1):
        #print("Total: ", total)
        total += int(student[i])

    return (student_name, total / 4)

student_report_data = []

for student_info in student_grades:
    #print(student_info)
    student_report_data.append(calculate_grade(student=student_info))
    #print(student_report_data)

print(student_report_data)
highest_grade = ["Name", 0]

for data in student_report_data:
    print(f"Name: {data[0]}, Grade: {data[1]}")

for i in range(0, len(student_report_data), 1):
    if highest_grade[1] < student_report_data[i][1]:
        highest_grade = list(student_report_data[i])

print(f"Highest Grade:\nName: {highest_grade[0]}, Grade: {highest_grade[1]}")
    
