"""Simulates the 'Ride the Bus' Game"""

import cards

def rtb_round1():
    """Round one of Ride the Bus: Black or Red"""
    global win_state
    card = deck.pop_card()
    #   Assign a color based on suit
    if card.suit_name == 'Spades' or card.suit_name == 'Clubs':
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
            print(card)
            print("That's right! Moving on...")
            round_cards.append(card)
            win_state = True
            active = False
        elif guess != color:
            print(card)
            print("That's incorrect. Restarting...")
            active = False

def rtb_round2():
    """Round two of Ride the Bus: Higher or Lower"""
    global win_state
    card = deck.pop_card()
    active = True
    #   Play round
    while active:
        guess = input(f"Higher or lower than {round_cards[0].rank}?\n\t")
        guess = guess.lower()
        if guess != 'lower' and guess != 'higher':
            print("That's not a valid entry. Please guess again.")
        elif (guess == 'lower' and card.rank < round_cards[0].rank or
                guess == 'higher' and card.rank > round_cards[0].rank):
            print(card)
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        elif card.rank == round_cards[0].rank:
            print(card)
            print("It's a tie! You lose. Restarting...")
            win_state = False
            active = False
        else:
            print(card)
            print("Incorrect! Restarting...")
            win_state = False
            active = False

def rtb_round3():
    """Round three of Ride the Bus: In Between or Outside"""
    global win_state
    card = deck.pop_card()
    #   Build a list of values from rounds 1 and 2
    c_ranks = []
    for c in round_cards:
        c_ranks.append(c.rank)
    #   Make sure list is low - high
    c_ranks = sorted(c_ranks)
    #   Play round
    active = True
    while active:
        guess = input(f"Inside or outside of {c_ranks[0]} and {c_ranks[1]}\n\t")
        guess = guess.lower()
        if guess != 'inside' and guess != 'outside':
            print("That's not a valid entry. Please guess again.")
        elif (guess == 'inside' and card.rank > c_ranks[0] and
                card.rank < c_ranks[1]):
            print(card)
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        elif (guess == 'outside' and card.rank < c_ranks[0] or
                card.rank > c_ranks[1]):
            print(card)
            print("Correct! Moving on...")
            round_cards.append(card)
            active = False
        else:
            print(card)
            print("Incorrect! Restarting...")
            win_state = False
            active = False

def rtb_round4():
    """Round 4 of Ride the Bus: Suit"""
    global win_state
    card = deck.pop_card()
    #   Play round
    active = True
    while active:
        guess = input("Guess a suit.\n\t")
        guess = guess.lower()
        if guess not in ['spades', 'hearts', 'clubs', 'diamonds']:
            print("That's not a valid entry. Please guess again")
        elif guess == card.suit_name.lower():
            print(card)
            print("Correct!")
            round_cards.append(card)
            active = False
        elif guess != card.suit_name.lower():
            print(card)
            print("Incorrect! Restarting...")
            win_state = False
            active = False


deck = cards.Deck()
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
