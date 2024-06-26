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
chosen_word = random.choice(word_list)
print(f"The random word chosen is {chosen_word}")

# User input
guess = input("Please guess a letter ").lower()
print(f"You entered {guess} of type {type(guess)}")

# Now check the guess against the string
check_result = chosen_word.find(guess)

if chosen_word.find(guess) != -1:
    number_of_results = chosen_word.count(guess)
    print(f"Correct guess with {number_of_results} characters")
else:
    print("Your guess is not in the chosen word")

# Now show checking against each character
for index in chosen_word:
    if guess == index:
        check_guess = "right"
    else:
        check_guess = "wrong"
    print(f"{index}: {check_guess}")
