'''Making Carrot in A Box
    Player 2 has to guess if Player 1 telling truth or lie on 
    if he/she has the carrot in the box'''

print('Carrot In A Box by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random

def emptyBox():
    print('''Here are Two Boxes:
  __________      __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/ ''')
    return

print('Press Enter to begin the Game!!')

p1Name = input('Enter Player 1 Name: ')
p2Name = input('Enter Player 2 Name: ')
playerName = p1Name[:11].center(11) + '     ' + p2Name[:11].center(11)
    
emptyBox()
print(playerName)

print()
print(p1Name + ', you have a red box in front of you.')
print(p2Name + ', you have a gold box in front of you.')
print()
print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and do not look!!!')
input('When ' + p2Name + ' has closed their eyes, press Enter...')
print()

print(p1Name + 'here is the inside of your box.')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
          
          (carrot!)''')
    
    print(playerName)
else:
    print('''
(no carrot!)''')
    print(playerName)

    