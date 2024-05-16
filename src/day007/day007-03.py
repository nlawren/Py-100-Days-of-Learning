import random

# Day 7 Hangman Project task 3

word_list = ["aardvark", "baboon", "camel"]

print("Day 7 - Hangman Challenge - Task 2\n")
print(f"There are {len(word_list)} words.")
print("The list of words are: ")
for word in word_list:
    print(f" {word}")
chosen_word = random.choice(word_list)
print(f"The random word chosen is {chosen_word}")

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
# with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(f"Display string initially is: {display}")

# User input
guess = input("Please guess a letter: ").lower()
print(f"You entered {guess} of type {type(guess)}")

# Now check the guess against the string
check_result = chosen_word.find(guess)
if chosen_word.find(guess) != -1:
    number_of_results = chosen_word.count(guess)
    print(f"Correct guess with {number_of_results} characters")
else:
    print("Your guess is not in the chosen word")

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple",
# then display should be ["_", "p", "p", "_", "_"].
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print(f"Current position: {position}\t Current letter {letter} is a match")
    else:
        print(f"Current position: {position}\t Current letter {letter} is not a match")

# TODO-3: - Print 'display' and you should see the guessed letter in the
# correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter.
# We'll tackle that in step 3.
print(f"\nFinal display result is {display}\n")
