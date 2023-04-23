import random
from hangman_words_list import words
import string

"""
Ali Alzurufi

This program is an interactive implementation of the popular word-guessing game, Hangman. 
The player is presented with a random word, and they must try to guess the letters of the word, one at a time. 
The program keeps track of the player's correct and incorrect guesses and displays the word with the correctly guessed letters filled in. 
The player has a limited number of incorrect guesses before the game is over. 

Date: 02/22/23

"""


def get_word(words):
    """
    Generate random words from imported hangman_words_list file
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def play_game():
    """
    This function plays the game of hangman, where the player tries to guess a word by entering letters.
    """

    # Initialize variables for the game
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    # Loop through and display message and letters used so far
    while len(word_letters) > 0 and lives > 0:
        print(
            f'You have {lives} lives and you have used these letters: {" ".join(used_letters)}')
        print()

        # Display the current word with letters that have been guessed and hidden letters
        wordList = [
            letter if letter in used_letters else '-' for letter in word]
        print(f'Current word: {" ".join(wordList)}')

        # Prompt the user to enter a letter and validate the input
        guessed_letter = input("Guess a letter: ").upper()

        # Check if the guessed letter is in the word and update the variables accordingly
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)

            else:
                lives -= 1
                print("Letter is not in word")
                print()

        # Check if the letter has already been used before
        elif guessed_letter in used_letters:
            print("You have used that character")

        # Check if the input is invalid
        else:
            print("Invalid input. Try again")

    # Display the results to the user
    if lives == 0:
        print(f"You died! The word was {word}")
    else:
        print(f"You guessed it right! It was {word}")


play_game()
