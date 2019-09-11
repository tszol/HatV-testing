"""Simulates the 'Ride the Bus' Game"""

import carddeck

def rtb_round1():
    """Round one of Ride the Bus: Black or Red"""
    global win_state
    card = deck.cards.pop()
    #   Assign a color based on suit
    if card.suit == 'spades' or card.suit == 'clubs': 
        color = 'black'
    else:
        color = 'red'
    #   Play round
    active = True
    while active:
        guess = input("Guess a color: Black or Red? \n\t")
        guess = guess.lower()
        if guess != 'black' and guess != 'red':
            print("That's not a valid entry. Please guess again.")
        elif guess == color:
            card.show()
            print("That's right! Moving on...")
            round_cards.append(card)
            win_state = True
            active = False
        elif guess != color:
            card.show()
            print("That's incorrect. Restarting...")
            active = False

def rtb_round2():
    """Round two of Ride the Bus: Higher or Lower"""
    global win_state
    card = deck.cards.pop()
    print("Round 2:")
    active = True
    #   Play round
    while active:
        guess = input(f"Higher or lower than {round_cards[0].value}?\n\t")
        guess = guess.lower()
        if guess != 'lower' and guess != 'higher':
            print("That's not a valid entry. Please guess again.")
        elif (guess == 'lower' and card.value < round_cards[0].value or 
                guess == 'higher' and card.value > round_cards[0].value):
            card.show()
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        elif card.value == round_cards[0].value:
            card.show()
            print("It's a tie! You lose. Restarting...")
            win_state = False
            active = False
        else:
            card.show()
            print("Incorrect! Restarting...")
            win_state = False
            active = False

def rtb_round3():
    """Round three of Ride the Bus: In Between or Outside"""
    global win_state
    card = deck.cards.pop()
    #   Build a list of values from rounds 1 and 2
    c_values = []
    for c in round_cards:
        c_values.append(c.value)
    #   Make sure list is low - high
    c_values = sorted(c_values)
    print("Round 3:")
    #   Play round
    active = True
    while active:
        guess = input(f"Inside or outside of {c_values[0]} and {c_values[1]}\n\t")
        guess = guess.lower()
        if guess != 'inside' and guess != 'outside':
            print("That's not a valid entry. Please guess again.")
        elif (guess == 'inside' and card.value > c_values[0] and 
                card.value < c_values[1]):
            card.show()
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        elif (guess == 'outside' and card.value < c_values[0] or
                card.value > c_values[1]):
            card.show()
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        else:
            card.show()
            print("Incorrect! Restarting...")
            win_state = False
            active = False

def rtb_round4():
    """Round 4 of Ride the Bus: Suit"""
    global win_state
    card = deck.cards.pop()
    print("Round 4:")
    #   Play round
    active = True
    while active:
        guess = input("Guess a suit.\n\t")
        guess = guess.lower()
        if guess not in ['spades', 'hearts', 'clubs', 'diamonds']:
            print("That's not a valid entry. Please guess again")
        elif guess == card.suit:
            card.show()
            print("Correct!")
            round_cards.append(card)
            active = False
        elif guess != card.suit:
            card.show()
            print("Incorrect! Restarting...")
            win_state = False
            active = False


deck = carddeck.Deck()
deck.shuffle()
round_cards = []
win_state = False
rtb_round1()
if win_state == True:
    rtb_round2()
else:
    pass
if win_state == True:
    rtb_round3()
else:
    pass
if win_state == True:
    rtb_round4()
else:
    pass
if win_state == True:
    print("Congratulations! You won!")
