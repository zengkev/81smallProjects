'''Dice Roller: Create 4 to n sided dice for DnD'''

print('By Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import sys, random

print('''
Enter what kind and how many dice to roll. The format is the number o fdice, followed by "d", 
      followed by the number of sides the dice have. 
      You can also add a plus or minus adjustments

      Example: 
      3d6 rolls three 6 sided dices
      1d10+2 rolls one 10 sided dice and adds 2
      2d40-1 rolls two 40 sided dice and minus 1
      QUIT quits the program
''')

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!!')
            sys.exit()
        diceStr = diceStr.lower().replace(' ', '')
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')
        
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Find if there is a plus or minus sign for a modifier
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')
        
        # Find the number of sides (The '5' in '2d5+1')
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # find the modifier amount
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount
        
        # Simulate the dice rolls
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)
        
        print('TOtal:', sum(rolls) + modAmount, '(Each die:', end='')

        # Display each rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Display the modifier amount
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')
    
    except Exception as exc:
        print('Invalid Input. Enter something like "3d6" or "2d23+2".')
        print('INput was invalid because: ' + str(exc))
        continue