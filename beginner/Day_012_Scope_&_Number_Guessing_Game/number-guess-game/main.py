# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def set_difficulty() -> int:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess: int, answer: int, turns: int) -> int:
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def game():
    # print(logo)
    print("Welcome to the Number Guessing Game!")
    guessed_number = random.randint(1, 100)
    print(f"The correct answer is: {guessed_number}")

    turns = set_difficulty()
    is_game_over = False

    while not is_game_over:
        print(f"You have {turns} attempts remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        turns = check_answer(user_guess, guessed_number, turns=turns)

        if turns == 0:
            print("You loose.")

        is_game_over = (user_guess == guessed_number) or (turns == 0)


game()
