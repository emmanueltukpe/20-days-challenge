import random
import re
import sys


words = ["Antartica", "Mississippi", "Opulent", "Capricious", "Xenophobe"]
chosen_word = random.choice(words).upper()

def play_hangman(chosen_word):
    answer = {}
    for letter in chosen_word:
        answer[letter] = False
    guessed = False
    guessed_letter = []
    tries = 0
    
    while not guessed:
        print("Let's play hangman!")
        print("\n")
        tries += 1
        guess = input("Please guess a letter: ").upper()
        
        if tries == 1:
            print (f"You have made {tries} try")
        else:
            print (f"You have made {tries} tries")

        if guess == "!":
            print(answer)
            sys.exit(0)

        else:
            print("Press ! to exit game")           
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letter:
                    print("You already guessed the letter", guess)

                elif guess not in chosen_word:
                    print(guess, "NO")
                    guessed_letter.append(guess)

                else:
                    guessed_letter.append(guess)
                    guessed_index = [n for n in range(
                        len(chosen_word)) if chosen_word.find(guess, n) == n]
                    print("YES", guessed_index)
                    answer[guess] = True

            else:
                print("NO")


print(play_hangman(chosen_word))