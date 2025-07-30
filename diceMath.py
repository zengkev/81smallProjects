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
while time.time() < startTime + QUIZ_DURATION:
    # start the timer and main loop
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])
        sumAnswer += die[1]
    
    # Contains (x, y) tuples to the top left corner of each die
    topLeftDiceCorner = []
    for i in range(len(diceFaces)):
        while True:
            # place dice randomly on canvas
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
            # Get the coordinates for all four corners
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # check if this die overlaps with previous dice
            overlaps = False
            for prevDiceLeft, prevDiceTop in topLeftDiceCorner:
                prevDiceRight = prevDiceLeft + DICE_WIDTH
                prevDiceBottom = prevDiceTop + DICE_HEIGHT
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDiceLeft <= cornerX < prevDiceRight
                        and prevDiceTop <= cornerY < prevDiceBottom):
                        overlaps = True
            if not overlaps:
                topLeftDiceCorner.append((left, top))
                break
    # draw the dice on the canvas
    canvas = {}
    for i, (diceLeft, diceTop) in enumerate(topLeftDiceCorner):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = diceLeft + dx
                canvaxY = diceTop + dy
                canvas[(canvasX, canvaxY)] = dieFace[dy][dx]

    # Display the canvas on the screen
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
            print()
    # Let the player enter their answers
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correct += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrect += 1

# Display the final scores

