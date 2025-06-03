'''Boucing DVD Logo Jing Wei Zeng'''

import sys, random, time

try:
    import bext
except ImportError:
    print("Requires Bext module and install via: ")
    print("https://pypi.org/project/Bext/ or pip install Bext") 
    sys.exit

# Set up screensize

WIDTH, HEIGHT = bext.size()

# Boundary on Width to reduce new line
WIDTH -= 1

numberOfLogos = 5 # adjustable 
pauseAmount = .2
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# Adding direction of movement
upRIGHT ='ur'
upLeft = 'ul'
downRight = 'dr'
downLeft = 'dl'
directions = (upRIGHT, upLeft, downRight, downLeft)

# Key names for DVD dictionary

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate logos
    logos = []
    for i in range(numberOfLogos):
        logos.append({COLOR: random.choice(colors),
                     X: random.randint(1, WIDTH - 4),
                     Y: random.randint(1, HEIGHT - 4),
                     DIR: random.choice(directions)})
        if logos[-1][X] % 2 == 1:
            # making sure X is even so it will hit the corner
            logos[-1][X] -=1

    cornerBounces = 0 # Count times a logo hits the corner
    while True:
        for logo in logos:
            




# Start the program but CTRL C to stop

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing Logo by Jing Wei Zeng')
        sys.exit() 