'''Dice Math: Add up the Dice ASAP'''

print('By Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random, time

# Set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # space to display the sum

# Set up the durations
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6
REWARD = 4
PENALTY = 1
# Draw Dice Faces
assert MAX_DICE <= 14

D1 = (['+-------+'
       '|       |'
       '|   0   |'
       '|       |'
       '+-------+', 1])

D2a = (['+-------+'
        '| 0     |'
        '|       |'
        '|     0 |'
        '+-------+', 2])

D2b = (['+-------+'
        '|     0 |'
        '|       |'
        '| 0     |'
        '+-------+', 2])

D3a = (['+-------+'
        '| 0     |'
        '|   0   |'
        '|     0 |'
        '+-------+', 3])

D3b = (['+-------+'
        '|     0 |'
        '|   0   |'
        '| 0     |'
        '+-------+', 3])

D4 = (['+-------+'
       '| 0   0 |'
       '|       |'
       '| 0   0 |'
       '+-------+', 4])

D5 = (['+-------+'
       '| 0   0 |'
       '|   0   |'
       '| 0   0 |'
       '+-------+', 5])

D6a = (['+-------+'
        '| 0   0 |'
        '| 0   0 |'
        '| 0   0 |'
        '+-------+', 6])

D6b = (['+-------+'
        '| 0 0 0 |'
        '|       |'
        '| 0 0 0 |'
        '+-------+', 6])

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

# How to play the game message
print('''How to play? Add up the sides of all the dices.
        You have {} seconds to answer as much as possible.
      You get {} pointsfor each correct
      You get {} points for each incorrect'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# Keep track of how many answers were correct and incorrect
correct = 0
incorrect = 0
startTime = time.time()

    # start the timer and main loop

    # draw the dice on the canvas


    # Display the canvas on the screen

    # Let the player enter their answers


# Display the final scores

