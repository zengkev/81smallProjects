'''Conway's Game of Life
    Living cells with two or three neighbors stay alive
    Dead cells with exactly three neighbors turn alive
    All else dies or stays dead'''

print('Conway\'s Game of Life by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import copy, random, sys, time

WIDTH = 79
HEIGHT = 20

ALIVE = 'O'
DEAD = ' '
nextCells = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:

    print('\n' * 50)
    cells = copy.deepcopy(nextCells)

    # Print the cells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x, y], end='')
        print()
    print('Press Ctrl+C to quit')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbor's coordination 
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the numbers of neighbors
            numNeighbors = 0
            if cells[left, above] == ALIVE:
                numNeighbors += 1
            if cells[x, above] == ALIVE:
                numNeighbors += 1
            if cells[right, above] == ALIVE:
                numNeighbors += 1
            if cells[left, y] == ALIVE:
                numNeighbors += 1
            if cells[right, y] == ALIVE:
                numNeighbors += 1
            if cells[left, below] == ALIVE:
                numNeighbors += 1
            if cells[x, below] == ALIVE:
                numNeighbors += 1
            if cells[right, below] == ALIVE:
                numNeighbors += 1

            # Apply the algorithm
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(2)
    except KeyboardInterrupt:
        print("Game of Life")
        sys.exit()
