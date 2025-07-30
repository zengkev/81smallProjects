'''Collatz sequence 3n + 1 problem
    n >= 1
    n = n / 2 if n is even
    n = n * 3 + 1 '''

print('Collatz sequence by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import sys, time

print('Enter the starting number (non zero) or quit')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter a number greater than zero')
    sys.exit()

n = int(response)
print(n, end='', flush=True)

while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    
    print(', ' + str(n), end='', flush=True)
    time.sleep(0.5)
print()
