
import csv

# CUL-CYB 371 - Data Mining and Data Warehousing
# Fictional Student Dataset

students = [
    ["STU001", "Computer Science", 300, 85, 78],
    ["STU002", "Cyber Security", 200, 90, 82],
    ["STU003", "Information Technology", 100, 75, 65],
    ["STU004", "Computer Science", 400, 95, 88],
    ["STU005", "Cyber Security", 300, 80, 72],
    ["STU006", "Information Technology", 200, 70, 60],
    ["STU007", "Computer Science", 200, 88, 91],
    ["STU008", "Cyber Security", 100, 65, 55],
    ["STU009", "Information Technology", 300, 92, 85],
    ["STU010", "Computer Science", 100, 78, 70],
    ["STU011", "Cyber Security", 400, 96, 89],
    ["STU012", "Information Technology", 400, 82, 76],
    ["STU013", "Computer Science", 300, 90, 84],
    ["STU014", "Cyber Security", 200, 73, 68],
    ["STU015", "Information Technology", 100, 87, 80]
]

# Create CSV file
with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score"
    ])

    writer.writerows(students)

print("Student dataset created successfully!")

# Display dataset information
print("Total number of students:", len(students))

average_score = sum(student[4] for student in students) / len(students)

average_attendance = sum(student[3] for student in students) / len(students)

print("Average examination score:", round(average_score, 2))
print("Average attendance:", round(average_attendance, 2), "%")
