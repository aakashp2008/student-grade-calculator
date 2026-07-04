print("=== Student Grade Calculator ===")

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)
