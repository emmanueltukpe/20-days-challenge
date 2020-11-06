import random


def get_target_words():
    # this generates a word at random for the hangman game

    library = open('data/words.txt', "r")

    words_in_list = library.readlines()
    words = []

    for word in words_in_list:
        words.append(word.strip())

    chosen_word = random.choice(words).upper() 
    library.close()
    return chosen_word
chosen_word = get_target_words()
