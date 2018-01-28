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
        return self.value % 13

class CardDealer:
    """Class representing a casino card dealer"""

    def __init__(self):
        self.rng = RandomNumberGenerator()

    def draw_card(self):
        """Draw a random card, print the result, and return the result"""

        card = self.rng.generate(0, 51)

        return Card(card)

    def draw_cards(self, number):
        cards = []

        while (len(cards) < number):
            card = self.draw_card()
            isCardPresent = False
            
            for c in cards:
                if c.value == card.value:
                    isCardPresent = True
            
            if not isCardPresent:
                cards.append(card)
        
        return cards

class RandomNumberGenerator:
    """Class for a generator of random numbers"""

    def __init__(self):
        pass

    def generate(self, min, max):
        """Generates a random integer between min and max (endpoints
        included)"""

        return random.randint(min, max)
