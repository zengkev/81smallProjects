<<<<<<< HEAD
<<<<<<< HEAD
'''Let's play some Black Jack by Jing Wei Zeng'''

print('Linkedin: https://www.linkedin.com/in/zengkev/')

=======
'''Let's play some Black Jack'''
>>>>>>> b6747c44b6259022f16813e27d0f95f5da950ee8
=======
'''Let's play some Black Jack'''
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75

import random, sys

Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)
Backside = 'backside'

# main part: start off with 50000 and play the logic of the game

def main():
    print("Blk Jack by Jing Wei Zeng")

    '''Rules:
        1. Get close to 21 as much as possible
        2. Kings, Queen and Jack = 10 points
        3. Acess is 1 or 11
        4. Cards 2 to 10 at face value
        5. (H) is deal one more card
        6. (S) is hold your hand
        7. (D) Double down your bet 
                Only one first (H) EXACTLY one more time then (S) hold
        8. If tie, bet is return to player
        9. Dealer stops at 17 '''
    

    # initialize
    yourMoney = 50_000
    while True:
        if yourMoney <= 0:
            print("Ya Broke dude!!")
            print("Don't worry, it's not realy $$")
            sys.exit()
        
        # Let's play the game
        print("Your Money: ${}".format(yourMoney))
        bet = getBet(yourMoney) #Ask how much you want to bet

        # Let's deal the hand but we need a deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

<<<<<<< HEAD
<<<<<<< HEAD
        break
=======
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75
        # Handle the player's actions
        print('Player bet:', bet)
        while True:
            displayHands(playerHand, dealerHand, False) #refer to function displayHands
            print()

            # Check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move: H, S, or D
            move = getMove(playerHand, yourMoney - bet)

            # Handle Player moves
            if move == 'D':
                additionalbet = getBet(min(bet, (yourMoney - bet))) # bet up to available fund
                bet += additionalbet
                print('Bet increase to {}.'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ('S', 'D'):
                break

        # Handle dealer hand

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # dealer draw another card
                print('Dealer Hits.....')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
            
                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        # show final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print('Dealer busted: You win ${}'.format(bet))
            yourMoney += bet
        elif (playerValue > 21) or playerValue < dealerValue:
            print('Dealer wins: You lost ${}'.format(bet))
            yourMoney -= bet
        elif playerValue > dealerValue:
            print('You win ${}'.format(bet))
            yourMoney += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you')
        
        input('Press Enter to play again')
        print('\n\n')
                
<<<<<<< HEAD
>>>>>>> b6747c44b6259022f16813e27d0f95f5da950ee8
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75
def getBet(maxBet):
    while True:
        print('How much do you want to bet? (1 to {}, or QUIT)'.format(maxBet))
        bet = input('I will bet: ').upper().strip()
        if bet == 'QUIT':
            print('Good Choice!!')
            sys.exit()
        #Now you bet an amount
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #Now we have a bet amount

def getDeck():
    '''Return a randomized deck'''
    deck = []
    for suit in (Hearts, Diamonds, Spades, Clubs):
        for rank in range(2, 11): # 9 non face cards
<<<<<<< HEAD
<<<<<<< HEAD
            deck.append(str(rank), suit)
        for rank in ('J', 'Q', 'K', 'A'): # Face and Ace cards
            deck.append(str(rank),suit)
    return random.shuffle(deck)



        

=======
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'): # Face and Ace cards
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    #Show dealer hand
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand) #pictures of the cards
    else:
        print('Dealer: ???')
        displayCards([Backside] + dealerHand[1:])

    #Show player Hand
    print('Player:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    '''Return card value that is dealt'''
    value = 0
    numberOfAces = 0

    # Add the non Aces value and keep a count on numberOfAces
    for card in cards:
        rank = card[0] # in getDeck we return deck card as (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)
    
    # deal with the numberOfAces
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10 # count ace as 11 if it's still under 21
    
    return value

def displayCards(cards):
    ''' Return card image '''
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == Backside:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '| ##| '
        else:
            rank, suit = card # card structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))    
    for row in rows:
        print(row)


def getMove(playerHand, yourMoney):
    '''Return input move back'''
    while True:
        moves = ['(H)it', '(S)tand']

        # Only can (D)ouble down when initial aka 2 cards and has money
        if len(playerHand) == 2 and yourMoney > 0:
            moves.append('(D)ouble')
        
        # Get the player's move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move ==  'D' and '(D)ouble' in moves:
            return move
        
<<<<<<< HEAD
>>>>>>> b6747c44b6259022f16813e27d0f95f5da950ee8
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75

# initialize the main function and run the program
if __name__ == '__main__':
    main()