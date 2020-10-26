import random
import re
import sys
import glob
import os


def get_target_words():
    # this generates a word at random for the hangman game

    library = open('hangman/data/words.txt', "r")

    words_in_list = library.readlines()
    words = []

    for word in words_in_list:
        words.append(word.strip())

    chosen_word = random.choice(words).upper()
    library.close()
    return chosen_word


class Hangman:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.answers = {}
        self.check_answers = {}
        self.answer = "_" * len(self.chosen_word)
        self.guess = ''

    def hangman_algorithm(self):
        # the random word generated is stored in a dictionary
        # all the characters in the word are set to false

        for letter in self.chosen_word:
            self.answers[letter] = False
        return self.answers

    def check_function(self):
        for letter in self.chosen_word:
            self.check_answers[letter] = True
        return self.check_answers

    def display_current_guess(self):
        # The function also takes correct guesses and prints out the position of each guesssed letter.

        word_as_list = list(self.answer)
        guessed_index = [
            i for i, letter in enumerate(self.chosen_word)
            if letter == self.guess
        ]
        for letter in guessed_index:
            word_as_list[letter] = self.guess
        self.answer = "".join(word_as_list)
        return self.answer

    def input_check(self):
        guess_check = "[^a-zA-Z!]"
        if (re.search(guess_check, self.guess)):
            return True
        return False

    def play_hangman(self):
        # takes input from the user, enabling him to play hangman.

        guessed = False
        guessed_letter = []
        self.answers = self.hangman_algorithm()
        self.check_answers = self.check_function()
        tries = 5
        print("Let's play hangman!")
        print("You have 5 tries, goodluck")
        print(self.answer)
        print("\n")

        while not guessed and tries > 0:

            self.guess = input("Please guess a letter: ").upper()

            if self.input_check() or len(self.guess) > 1:
                print(
                    "Your input must be a single character alphabet or '!' to exit"
                )
            elif self.guess == "!":
                print(
                    f"The word was {self.chosen_word}. Better luck next time")
                sys.exit(0)

            else:
                print("Press ! to exit game")
                if len(self.guess) == 1 and self.guess.isalpha():
                    if self.guess in guessed_letter:
                        tries -= 1
                        print("You already guessed the letter")
                        if tries == 1:
                            print(f'You have only a try left')
                        else:
                            print(f'You have {tries} tries left')

                    elif self.guess not in self.chosen_word:
                        tries -= 1
                        print(self.guess)
                        if tries == 1:
                            print(f'Oops you are wrong, You have only a try left')
                        else:
                            print(
                                f'Oops you are wrong, You have {tries} tries left')
                        guessed_letter.append(self.guess)

                    else:
                        guessed_letter.append(self.guess)
                        self.answers[self.guess] = True
                        self.answer = self.display_current_guess()
                        if self.answers == self.check_answers:
                            guessed = True

            print(self.answer)
            print("\n")

        if guessed:
            print("Congrats, you've guessed the word! You won!")
        else:
            print("Sorry, you've run out of tries. The word was " +
                  chosen_word + ". Maybe next time!")


chosen_word = get_target_words()
hangman = Hangman(chosen_word)
hangman.play_hangman()
