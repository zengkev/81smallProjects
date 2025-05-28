"""Bagels
A logic game where you must guess a number based on clues"""

import random

# Init

GUESS_DIGITS = 3 # Try 1 to 10
MAX_GUESSES = 10 # Try 1 to 30

def main():

    print('''Bagels, a deductive logic game. 
          requirement: 1. digit not repeat and random
          clues: When I say: That means:
            Pico     One digit is correct but in the wrong position
            Fermi    One digit is correct and in the correct position
            Bagels   No digit is correct'''.format(GUESS_DIGITS))
    
    while True: 
        # This stores the secret number by random
        secretNum = getSecretNum()
        print('I have a number in mind.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        # Start guessing
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != GUESS_DIGITS or not guess.isdigit():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            

# initialize the main function and run the program
if __name__ == '___main__':
    main()