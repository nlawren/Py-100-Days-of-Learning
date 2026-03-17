# Day 9 Dictionaries
# Coding Exercise 9

student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name, score in student_scores.items():
    print(f"Assessing {name} with a score of {score}")
    if score > 90 and score <= 100:
        grade = "Outstanding"
    elif score > 80 and score <= 90:
        grade = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[name] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
