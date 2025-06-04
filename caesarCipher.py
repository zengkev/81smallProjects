'Casear Cipher by Jing Wei Zeng'
'''
try:
    import pyperclip
except ImportError:
    pass
'''
import string

SYMBOLS =  string.ascii_uppercase + string.digits + string.punctuation

print("Ceasear Cipher encrypts by shifting the letter over.")

print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

while True: 
    maxKey = len(SYMBOLS) - 1
    print('Please enter a digit between 1 and {}.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message you want to {}:'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        translated += symbol

print("{}ed message: ".format(mode) + translated)
'''
try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass
'''
