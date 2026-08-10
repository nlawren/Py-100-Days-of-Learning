# 🚨 Don't change the code below 👇
raw_heights = input("Input a list of student heights: ").split()
student_heights = [int(h) for h in raw_heights]
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

total_height = 0
num_students = 0

for height in student_heights:
    total_height += height
    num_students += 1

average_height = round(total_height / num_students)

print(average_height)
