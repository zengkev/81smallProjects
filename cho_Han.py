'''What is cho han? A dice game where two
    six sided dice rolled in a cup and 
    gamblers must guess the sum.
    even = cho
    odd = han'''

print('Cho Han by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random, sys

# Dice, and starting
rollingDice = {1: 'ICHI', 2: 'NI', 3: 'SAN',
               4: 'SHI', 5: 'GO', 6: 'ROKU'}

purse = 5000

# loop the main game
while True:
    # start the bet
    print('You have', purse, 'mon. How much do you bet? or (QUIT)')
    while True:
    # Start the game with input or quit
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing')
            sys.exit
        elif not pot.isdecimal():
            print('Must enter a number')
        elif int(pot) > purse:
            print('You do not have enough')
        else:
            # continue to game
            pot = int(pot)
            break
    
    # Let's roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('Dealer: Swirls the cup and slams the cup but still covering the dice.')
    print('Dealer: dice is set and place your bet!!')
    print()
    print()
    print('     CHO (even) or HAN (odd)?')

    while True:
        # bet is even or odd
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Only bet "CHO" or "HAN"!!')
            continue
        else:
            break

    print('Dealer lifts the cup!!')
    print('  ', rollingDice[dice1], '-', rollingDice[dice2])
    print('     ', dice1, '-', dice2)

    # determine even or odd and who own
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        winningBet = 'CHO'
    else:
        winningBet = 'HAN'
    
    playerWon = bet == winningBet

    if playerWon:
        print('You Won!! You take', pot, 'mon.')
        print('House take 10% cut')
        purse += (pot - (pot // 10))
        print('You have ', purse, 'Now!!')
    else:
        print('Dealer Won!!')
        purse -= pot
        print('You have', purse, 'left.')

    if purse <= 0:
        print('Game Ends Here')

            