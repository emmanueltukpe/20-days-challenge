import re
import sys
from lib.utils import chosen_word
from lib.core import hangman_algorithm, check_function, input_check, display_current_guess



def play_hangman():
        # takes input from the user, enabling him to play hangman.

        guessed = False
        guessed_letter = []
        answers = hangman_algorithm()
        check_answers = check_function()
        answer = "_" * len(chosen_word)
        tries = 5
        print("Let's play hangman!")
        print("You have 5 tries, goodluck")
        print(answer)
        print("\n")

        while not guessed and tries > 0:

            guess = input("Please guess a letter: ").upper()

            if input_check() or len(guess) > 1:
                print(
                    "Your input must be a single character alphabet or '!' to exit"
                )
            elif guess == "!":
                print(
                    f"The word was {chosen_word}. Better luck next time")
                sys.exit(0)

            else:
                print("Press ! to exit game")
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letter:
                        tries -= 1
                        print("You already guessed the letter")
                        if tries is 1:
                            print(f'You have only a try left')
                        else:
                            print(f'You have {tries} tries left')

                    elif guess not in chosen_word:
                        tries -= 1
                        print(guess)
                        if tries is 1:
                            print(
                                f'Oops you are wrong, You have only a try left'
                            )
                        else:
                            print(
                                f'Oops you are wrong, You have {tries} tries left'
                            )
                        guessed_letter.append(guess)

                    else:
                        guessed_letter.append(guess)
                        answers[guess] = True
                        answer = display_current_guess()
                        if answers == check_answers:
                            guessed = True

            print(answer)
            print("\n")

        if guessed:
            print("Congrats, you've guessed the word! You won!")
        else:
            print("Sorry, you've run out of tries. The word was " +
                  chosen_word + ". Maybe next time!")

play_hangman()
