# 🚨 Don't change the code below 👇
raw_scores = input("Input a list of student scores ").split()
student_scores: list[int] = []
for n in range(len(raw_scores)):
    student_scores = [int(s) for s in raw_scores]
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
high_score = 0

for score in student_scores:
    high_score = max(high_score, score)

print(f"The highest score in the class is: {high_score}")
