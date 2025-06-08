'''bruteforce caesar cipher'''

import string

print('Caesar Cipher Hacker by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()
print('Enter the encrypted message to decrypt: ')
message = input('> ')

SYMBOLS =  string.ascii_letters + string.digits + string.punctuation
for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num -= key

            # Handle the wrap-around if num is less than 0
            if num < 0:
                num += len(SYMBOLS)

            # Add decrypted number's symbo to translated
            translated += SYMBOLS[num]
        else:
            translated += symbol

    print('Key #{}: {}'.format(key, translated))

