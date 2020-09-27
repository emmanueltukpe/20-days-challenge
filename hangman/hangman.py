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
chosen_word = get_target_words()



def hangman_algorithm():
    # the random word generated is stored in a dictionary
    # all the characters in the word are set to false

    answers = {}
    for letter in chosen_word:
        answers[letter] = False
    return answers
answers = hangman_algorithm()

def check_function():
    check_answers = {}
    for letter in chosen_word:
        check_answers[letter] = True
    return check_answers
check_answers = check_function()

def display_current_guess(answer, chosen_word, guess):
    #The function also takes correct guesses and prints out the position of each guesssed letter.
    

    word_as_list = list(answer)
    guessed_index = [i for i, letter in enumerate(chosen_word) if letter == guess]
    for letter in guessed_index:
        word_as_list[letter] = guess
    answer = "".join(word_as_list)
    return answer

def play_hangman(chosen_word):
    # takes input from the user, enabling him to play hangman.
    
    answer = "_" * len(chosen_word)
    guessed = False
    guessed_letter = []
    tries = 5
    print("Let's play hangman!")
    print("You have 5 tries, goodluck")
    print(answer)
    print("\n")

    while not guessed and tries > 0:

        guess = input("Please guess a letter: ").upper()
        
        if guess == "!":
            print(f"The word was {chosen_word}. Better luck next time")
            sys.exit(0)

        else:
            print("Press ! to exit game")           
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letter:
                    tries -= 1
                    print("You already guessed the letter")
                    if tries is 1:
                        print (f'You have only a try left')
                    else:
                        print(f'You have {tries} tries left')

                elif guess not in chosen_word:
                    tries -= 1
                    print(guess)
                    if tries is 1:
                        print (f'Oops you are wrong, You have only a try left')
                    else:
                        print(f'Oops you are wrong, You have {tries} tries left')
                    guessed_letter.append(guess)

                else:
                    guessed_letter.append(guess)
                    answers[guess] = True
                    answer = display_current_guess(answer, chosen_word, guess)
                    if answers == check_answers:
                        guessed = True

            else:
                tries -= 1
                if tries is 1:
                    print (f'Not valid, enter an actual letter!, You have only a try left')
                else:
                    print(f"Not valid, enter an actual letter! You have {tries} tries left")

        print(answer)
        print("\n")    
    if guessed:
         print("Congrats, you've guessed the word! You won!")
    else:
        print("Sorry, you've run out of tries. The word was " + chosen_word + ". Maybe next time!")

play_hangman(chosen_word)