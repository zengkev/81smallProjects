'''Diamonds: Draws ASCII art-diamonds of various size'''

print('By Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

def main ():
    for diamondSize in range(10, 20): 
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()
    
def displayOutlineDiamond(size): 
    for i in range(size): # top half
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    for i in range(size): # bottom half
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * (size - i - 1) * 2, end='')
        print('/')

def displayFilledDiamond(size):
    for i in range(size): # top half
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\'* (i + 1))

    for i in range(size): # bottom half
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))        

    

if __name__ == '__main__':
    main()


'''
change \\ to @ and see
change range(0, 6) to (0, 30)
remove for i in range(size)
'''