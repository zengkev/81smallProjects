'''Boucing DVD Logo Jing Wei Zeng'''
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
print('Linkedin: https://www.linkedin.com/in/zengkev/')

=======
>>>>>>> b6747c44b6259022f16813e27d0f95f5da950ee8
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75
>>>>>>> dev

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
            logos[-1][X] -= 1

    cornerBounces = 0 # Count times a logo hits the corner
    while True:
        for logo in logos:
            # earse the logo current location to check new coordination
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            # See if the logo bounces off the corner
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = downRight
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = upRIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = downLeft
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = upLeft
                cornerBounces += 1

            # Check if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == upLeft:
                logo[DIR] = upRIGHT
            elif logo[X] == 0 and logo[DIR] == downLeft:
                logo[DIR] = downRight

            # Check if the logo bounces off the right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == upRIGHT:
                logo[DIR] = upLeft
            elif logo[X] == WIDTH - 3 and logo[DIR] == downRight:
                logo[DIR] = downLeft
            
            # Check if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == upLeft:
                logo[DIR] = upRIGHT
            elif logo[Y] == 0 and logo[DIR] == downLeft:
                logo[DIR] = downRight

            # Check if the logo bounces off the bottom edge

            elif logo[Y] == HEIGHT - 1 and logo[DIR] == downLeft:
                logo[DIR] = upLeft
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == downRight:
                logo[DIR] = upRIGHT

            if logo[DIR] != originalDirection:
                # Change the color when bounces
                logo[COLOR] = random.choice(colors)

            # Moving the logos
            if logo[DIR] == upRIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == upLeft:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == downRight:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == downLeft:
                logo[X] -= 2
                logo[Y] += 1

            # Clamp positions to avoid negative y coordinates
            logo[X] = max(0, min(WIDTH - 3, logo[X]))
            logo[Y] = max(0, min(HEIGHT - 1, logo[Y]))

            # Display number of corners bounced
            bext.goto(5, 0)
            bext.fg('white')
            print('Corner Bounced: ', cornerBounces, end='')

            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[COLOR])
                print('DVD', end='')
            
        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(pauseAmount)

# Start the program but CTRL C to stop

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing Logo by Jing Wei Zeng')
        sys.exit() 