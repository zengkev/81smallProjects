'''Digit Stream: Neo @ it Again'''

print('By Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random, shutil, sys, time

Min_Stream_Length = 6
Max_Stream_Length = 14
Pause = 0.1
Stream_Char = ['0', '1']

# range from 0 to 1.0
Density = 0.02

# Get the size of the terminal window
Width = shutil.get_terminal_size()[0]
Width -= 1

print("Digit Stream like Matrix")
time.sleep(2)

try:
    columns = [0] *  Width
    while True:
        for i in range(Width):
            if columns[i] == 0:
                if random.random() <= Density:
                    columns[i] = random.randint(Min_Stream_Length, Max_Stream_Length)
            
            # Display empty or 1/0
            if columns[i] > 0:
                print(random.choice(Stream_Char), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush() # Make sure text appears on the screen.
        time.sleep(Pause)
except KeyboardInterrupt:
    sys.exit()
    
