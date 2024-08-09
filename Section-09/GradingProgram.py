student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# Create an empty dictionary to collect the new values.
student_grades = {}
for name, score in student_scores.items():
    if score >= 91 and score <=100:
        student_grades[name] = "Outstanding"
    elif score >= 81 and score < 91:
        student_grades[name] =  "Exceeds Expectations"
    elif score >= 71 and score < 81:
        student_grades[name] =   "Acceptable" 
    else:
        student_grades[name] =  "Fail"

for student in student_grades:
    print(f'{student} received a {student_grades[student]} grade ({student_scores[student]}).')