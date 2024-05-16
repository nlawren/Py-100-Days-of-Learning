import random

# Day 7 Hangman Project task 3

word_list = ["aardvark", "baboon", "camel"]

print("Day 7 - Hangman Challenge - Task 3\n")
print(f"There are {len(word_list)} words.")
print("The list of words are: ")
for word in word_list:
    print(f" {word}")
chosen_word = random.choice(word_list)
print(f"The random word chosen is {chosen_word}")

# Create the list with blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(f"Display string initially is: {display}")

# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all
# the letters in the chosen_word and 'display' has no more
#  blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    # User input
    guess = input("Please guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

print(f"\nFinal display result is {display}\nYou won!\n")
