import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

print("Day 7 - Hangman Challenge - Task 1\n")
print(f"There are {len(word_list)} words.")
print("The list of words are: ")
for word in word_list:
    print(f" {word}")
random_choice = random.randint(0, (len(word_list) - 1))
chosen_word = word_list[random_choice]
print(f"The random word chosen is {chosen_word}")
