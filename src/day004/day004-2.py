# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_candidates = len(names)
random_choice = random.randint(0, num_candidates-1)
person_paying = names[random_choice]
# print(candidates,names,person_paying)

# Output required
print(f"{person_paying} is going to buy the meal today!")
