"""Bagels
A logic game where you must guess a number based on clues"""

print('Linkedin: https://www.linkedin.com/in/zengkev/')

import random

# Init

GUESS_DIGITS = random.randint(1, 5) # Try 1 to 825
MAX_GUESSES = random.randint(6, 20) # Try 5 to 30

def main():

    print('''Bagels, a deductive logic game. 
          requirement: 1. digit not repeat and random
          clues: When I say: That means:
            Pico     One digit is correct but in the wrong position
            Fermi    One digit is correct and in the correct position
            Bagels   No digit is correct
          
          We want to you to guess {} digits for this game.'''.format(GUESS_DIGITS))
    
    while True: 
        # This stores the secret number by random
        secretNum = getSecretNum()
        print('I have a number in mind.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        # Start guessing
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != GUESS_DIGITS or not guess.isdigit():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum) # this should return example 'Pico, Fermi, or Bagels'
            print(clues)
            numGuesses += 1 # want to increment higher to Max Guesses end the loop

            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print("Sorry Game Over")
                print("Answer is {}.".format(secretNum))
        
        print("Do you want to play again? (yah or nah)")
        if not input('>').lower().startswith('y'):
            break
    
    print("Thanks for chillig")

def getSecretNum():
    '''Return a string made up of GUESS_DIGITS'''
    numbers = list('0123456789')
    random.shuffle(numbers) #shuffle but is this unqie?

    # Get the first 3 digits in the shuffle!! uniqueness
    secretNum = ''
    for i in range(GUESS_DIGITS): # give up to guess digits asked
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Return a string with the pico, fermi or bagels clues for the guess input'''
    if guess == secretNum:
        return "You got it"
    
    clues = []

    # say if guess is 123 and we take guess[0] = 1 == secretNum[0], then return pico, fermi or bagel
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    # Bagels cuz no guess is right
    if len(clues) == 0:
        return 'Bagels'
    else:
        # We want to put clues in a string. Sort cuz we want to make the game harder
        clues.sort()
        return ''.join(clues)
    
    


# initialize the main function and run the program
if __name__ == '__main__':
    main()