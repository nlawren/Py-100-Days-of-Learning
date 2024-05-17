import random

from hangman_art import logo, stages
from hangman_words import word_list

# Day 7 Hangman Project task 5
# Moving variables to files/modules (art and words)
# Tidying up the ux - providing hints and confirmation of previous guesses etc

print(logo)
print("Day 7 - Hangman Challenge - Task 5\n")
print(f"There are {len(word_list)} words.")
chosen_word = random.choice(word_list)
print(f"The random word chosen is {chosen_word}")

# Setup variables
end_of_game = False
lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    found = False
    if guess in display:
        print(f"You already guessed {guess}")
    # Check guess
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            found = True
    if not found:
        print(f"{guess} is not in the word")
        lives -= 1
        print(f"You have {lives} left")
    if lives == 0:
        print("You lose")
        end_of_game = True

    print(stages[lives])
    # Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # Check if user has guessed the whole word.
    if "_" not in display:
        end_of_game = True
        print("You win.")
