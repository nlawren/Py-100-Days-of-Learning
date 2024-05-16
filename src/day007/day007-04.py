import random

# Day 7 Hangman Project task 4

word_list = ["aardvark", "baboon", "camel"]

print("Day 7 - Hangman Challenge - Task 4\n")
print(f"There are {len(word_list)} words.")
print("The list of words are: ")
for word in word_list:
    print(f" {word}")
chosen_word = random.choice(word_list)
print(f"The random word chosen is {chosen_word}")

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


# Setup variables
end_of_game = False
lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    found = False
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            found = True
    if not found:
        lives -= 1
        print(f"You have {lives} left")
    if lives == 0:
        print("You lose")
        end_of_game = True

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
