from hangman_art import *
from hangman_words import *
import random
lives=6
print(logo)

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=""

for i in range(chosen_word.__len__()):
    placeholder=placeholder+"_"
print(placeholder)
gameover=False
correct_letters=[]
while not gameover:
    print(f"*****************************{lives}/6 lives left ************************************")
    guess_letter=input("Guess the letter = ").lower()
    if guess_letter is correct_letters:
        print(f"You guessed the correct letter {guess_letter}")
    display = ""
    for letter in chosen_word:
        if letter == guess_letter:
            display = display + letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+= letter
        else:
            display = display + "_"
    print(display)

    if guess_letter not in chosen_word:
        lives = lives - 1
        print(f"You guessed {guess_letter} that's not in the word you lose a live")
        if lives == 0:
            gameover = True
            print(f"*************************{chosen_word} you lose a live************************************")

    if "_" not in display:
        gameover = True
        print("you win")

    print(stages[lives])

