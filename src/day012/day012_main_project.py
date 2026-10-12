# Day 12 Main Project
# Number Guessing Game

from random import randint

LOWEST = 1
HIGHEST = 100
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
LEVELS = {"easy": EASY_LEVEL_TURNS, "hard": HARD_LEVEL_TURNS}


def check_guess(guess: int, answer: int) -> str:
    """Return "high", "low" or "correct" for a guess compared with the answer."""
    if guess > answer:
        return "high"
    if guess < answer:
        return "low"
    return "correct"


def parse_difficulty(text: str) -> int | None:
    """Return the turns for a difficulty name, or None if it isn't one."""
    return LEVELS.get(text.strip().lower())


def parse_guess(text: str) -> int | None:
    """Return the guess as an int if it's a whole number in range, else None."""
    try:
        guess = int(text)
    except ValueError:
        return None
    if LOWEST <= guess <= HIGHEST:
        return guess
    return None


def ask_difficulty() -> int:
    """Keep asking until the player types a valid difficulty."""
    while True:
        turns = parse_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))
        if turns is not None:
            return turns
        print("Please type 'easy' or 'hard'.")


def ask_guess() -> int:
    """Keep asking until the player types a valid guess."""
    while True:
        guess = parse_guess(input("Make a guess: "))
        if guess is not None:
            return guess
        print(f"Please enter a whole number from {LOWEST} to {HIGHEST}.")


def play(answer: int, turns: int) -> bool:
    """Play one game. Return True if the player guesses the answer in time."""
    while turns > 0:
        plural = "" if turns == 1 else "s"
        print(f"You have {turns} attempt{plural} remaining to guess the number.")
        result = check_guess(ask_guess(), answer)
        if result == "correct":
            print(f"You got it! The answer was {answer}.")
            return True
        turns -= 1
        print(f"Too {result}.")
        if turns > 0:
            print("Guess again.")
    print(f"You've run out of guesses. The answer was {answer}.")
    return False


def main() -> None:
    # Imported here, not at the top, so tests can import this module:
    # `art` is only findable when this file is run as a script.
    from art import logo

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOWEST} and {HIGHEST}.")
    play(randint(LOWEST, HIGHEST), ask_difficulty())


if __name__ == "__main__":
    main()
