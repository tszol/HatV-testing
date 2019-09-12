"""Simulates the 'Ride the Bus' Game"""

import cards


class RideTheBus:

    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.round_cards = []
        self.win_state = False

    def play(self):
        self.rtb_round1()
        if self.win_state == True:
            self.rtb_round2()
        else:
            pass

        if self.win_state == True:
            self.rtb_round3()
        else:
            pass

        if self.win_state == True:
            self.rtb_round4()
        else:
            pass

        if self.win_state == True:
            print("Congratulations! You won!")

    def rtb_round1(self):
        """Round one of Ride the Bus: Black or Red"""
        card = self.deck.pop_card()
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
                self.round_cards.append(card)
                self.win_state = True
                active = False
            elif guess != color:
                print(card)
                print("That's incorrect. Restarting...")
                active = False

    def rtb_round2(self):
        """Round two of Ride the Bus: Higher or Lower"""
        card = self.deck.pop_card()
        active = True
        #   Play round
        while active:
            guess = input(f"Higher or lower than {self.round_cards[0].rank}?\n\t")
            guess = guess.lower()
            if guess != 'lower' and guess != 'higher':
                print("That's not a valid entry. Please guess again.")
            elif (guess == 'lower' and card.rank < self.round_cards[0].rank or
                    guess == 'higher' and card.rank > self.round_cards[0].rank):
                print(card)
                print("Correct! Moving on...")
                self.round_cards.append(card)
                active = False
            elif card.rank == self.round_cards[0].rank:
                print(card)
                print("It's a tie! You lose. Restarting...")
                self.win_state = False
                active = False
            else:
                print(card)
                print("Incorrect! Restarting...")
                self.win_state = False
                active = False

    def rtb_round3(self):
        """Round three of Ride the Bus: In Between or Outside"""
        card = self.deck.pop_card()
        #   Build a list of values from rounds 1 and 2
        c_ranks = []
        for c in self.round_cards:
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
                self.round_cards.append(card)
                active = False
            elif (guess == 'outside' and card.rank < c_ranks[0] or
                    card.rank > c_ranks[1]):
                print(card)
                print("Correct! Moving on...")
                self.round_cards.append(card)
                active = False
            else:
                print(card)
                print("Incorrect! Restarting...")
                self.win_state = False
                active = False

    def rtb_round4(self):
        """Round 4 of Ride the Bus: Suit"""
        card = self.deck.pop_card()
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
                self.round_cards.append(card)
                active = False
            elif guess != card.suit_name.lower():
                print(card)
                print("Incorrect! Restarting...")
                self.win_state = False
                active = False


if __name__ == '__main__':
    game = RideTheBus()
    game.play()
