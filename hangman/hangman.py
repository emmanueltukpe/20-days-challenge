import random
import re


words = ["Antartica", "Mississippi", "Opulent", "Capricious", "Xenophobe"]
chosen_word = random.choice(words).upper()


def play_hangman(chosen_word):
    answer = ""
    guessed = False
    guessed_letter = []
    print("Let's play hangman!")
    print("\n")
    while not guessed:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in chosen_word:
                print(guess, "NO")
                guessed_letter.append(guess)

            else:
                guessed_letter.append(guess)
                guessed_index = [n for n in range(
                    len(chosen_word)) if chosen_word.find(guess, n) == n]
                print("YES", guessed_index)
                if " " not in answer:
                    guessed = True
        else:
            print("NO")
    return play_hangman(chosen_word)


print(play_hangman(chosen_word))
