#!/usr/bin/python3

import random

class CardDealer:
    """Class representing a casino card dealer"""

    def __init__(self):
        self.rng = RandomNumberGenerator()

    def draw_card(self):
        """Draw a random card, print the result, and return the result"""

        card = self.rng.generate(0, 51)

        suit = card // 13
        if suit == 0:
            suit_string = 'Clubs'
        elif suit == 1:
            suit_string = 'Diamonds'
        elif suit == 2:
            suit_string = 'Hearts'
        elif suit == 3:
            suit_string = 'Spades'
        else:
            raise AssertionError

        rank = card % 13
        if rank == 0:
            rank_char = 'A'
        elif rank == 10:
            rank_char = 'J'
        elif rank == 11:
            rank_char = 'Q'
        elif rank == 12:
            rank_char = 'K'
        else:
            rank_char = str(rank + 1)

        print('Card for dealer is the ' + rank_char + ' of ' + suit_string)

        return card

class RandomNumberGenerator:
    """Class for a generator of random numbers"""

    def __init__(self):
        pass

    def generate(self, min, max):
        """Generates a random integer between min and max (endpoints
        included)"""

        return random.randint(min, max)

DEALER = CardDealer()
for i in range(0, 100):
    DEALER.draw_card()
