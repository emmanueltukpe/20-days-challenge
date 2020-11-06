import re
from .utils import chosen_word

guess = ''
def hangman_algorithm():
        # the random word generated is stored in a dictionary
        # all the characters in the word are set to false

        answers = {}
        for letter in chosen_word:
            answers[letter] = False
        return answers

def check_function():

    check_answers = {}
    for letter in chosen_word:
        check_answers[letter] = True
    return check_answers

def display_current_guess():
    #The function also takes correct guesses and prints out the position of each guesssed letter.

    answer = "_" * len(chosen_word)
    word_as_list = list(answer)
    guessed_index = [
        i for i, letter in enumerate(chosen_word)
        if letter == guess
    ]
    for letter in guessed_index:
        word_as_list[letter] = guess
    answer = "".join(word_as_list)
    return answer
answer = display_current_guess()

def input_check():
    guess_check = "[^a-zA-Z!]"
    if (re.search(guess_check, guess)):
        return True
    return False