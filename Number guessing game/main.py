import random
from art import logo
#with using function

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()




















## without using function
'''
print(logo)

choice = random.randint(1, 100)

print("Welcome to the game!")

level = input("Easy or Hard: ").lower()

if level == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:

    print(f"You have {lives} lives left.")

    guess = int(input("Guess the number: "))

    if guess == choice:
        print("You Win!")
        break

    elif guess > choice:
        print("Too High")

    else:
        print("Too Low")

    lives -= 1

if lives == 0:
    print(f"You Lose! The number was {choice}")'''