#!/usr/bin/python3

import random

CLUBS = 0
DIAMONDS = 1
HEARTS = 2
SPADES = 3

class Card:

    def __init__(self, value):
        self.value = value

    def get_color(self):
        return self.value // 13

    def get_rank(self):
        return  self.value % 13

class CardDealer:
    """Class representing a casino card dealer"""

    def __init__(self):
        self.rng = RandomNumberGenerator()

    def draw_card(self):
        """Draw a random card, print the result, and return the result"""

        card = self.rng.generate(0, 51)

        # suit = card // 13
        # if suit == 0:
        #     suit_string = 'Clubs'
        # elif suit == 1:
        #     suit_string = 'Diamonds'
        # elif suit == 2:
        #     suit_string = 'Hearts'
        # elif suit == 3:
        #     suit_string = 'Spades'
        # else:
        #     raise AssertionError

        # rank = card % 13
        # if rank == 0:
        #     rank_char = 'A'
        # elif rank == 10:
        #     rank_char = 'J'
        # elif rank == 11:
        #     rank_char = 'Q'
        # elif rank == 12:
        #     rank_char = 'K'
        # else:
        #     rank_char = str(rank + 1)

        # print('Card for dealer is the ' + rank_char + ' of ' + suit_string)

        return Card(card)

    def draw_cards(self, number):
        cards = [0]*number

        currIndex = 0
        while (currIndex < number):
            card = self.draw_card()
            if not (card in cards):
                cards[currIndex]=card
                currIndex += 1
        
        return cards

class RandomNumberGenerator:
    """Class for a generator of random numbers"""

    def __init__(self):
        pass

    def generate(self, min, max):
        """Generates a random integer between min and max (endpoints
        included)"""

        return random.randint(min, max)