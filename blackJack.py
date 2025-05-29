'''Let's play some Black Jack'''

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

        break
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
            deck.append(str(rank), suit)
        for rank in ('J', 'Q', 'K', 'A'): # Face and Ace cards
            deck.append(str(rank),suit)
    return random.shuffle(deck)



        


# initialize the main function and run the program
if __name__ == '__main__':
    main()