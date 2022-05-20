student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]  # grade = value of Harry
    if score < 70:
        student_grades[student] = "Fail"
    elif score < 81:
        student_grades[student] = "Acceptable"
    elif score < 91:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)


