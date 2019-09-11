"""Stores classes for deck of cards"""

import random


class Card:
    def __init__(self, suit, value):
        """Initiates card with suit and value"""
        self.suit = suit
        self.value = value

    def show(self):
        """Displays card information"""
        print(f"{self.value} of {self.suit.title()}")


class Deck:
    def __init__(self):
        """initiates a Deck of cards"""
        self.cards = []
        self.build()

    def build(self):
        """Builds a deck of cards in order"""
        for s in ['spades', 'hearts', 'clubs', 'diamonds']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        """Shows entire deck"""
        for c in self.cards:
            c.show()

    def shuffle(self):
        """Shuffles deck"""
        self.cards = random.sample(self.cards, len(self.cards))

    def draw(self):
        """Draws top card from deck"""
        return(self.cards.pop().show())
