student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def grade(score):
    if score >= 91: return "Outstanding"
    elif score >= 81: return "Exceeds Expectations"
    elif score >= 71: return "Acceptable"
    else: return "Fail"

student_grades = {}

for name, score in student_scores.items():
    student_grades[name] = grade(score)