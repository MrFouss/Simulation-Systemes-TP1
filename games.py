#!/usr/bin/python3

from abc import ABCMeta
from card_dealer import * 

def playGame1(cardDealer):
    card = cardDealer.draw_card()
    if (card.get_rank() == 0):
        return True
    return False

def playGame2(cardDealer):
    card1 = cardDealer.draw_card()
    card2 = cardDealer.draw_card()
    if (card1.value == card2.value):
        return True
    return False

def playGame3(cardDealer):
    cards = cardDealer.draw_cards(2)
    if (cards[0].get_rank() < cards[1].get_rank()):
        return True
    return False

def playGame4(cardDealer):
    cards = cardDealer.draw_cards(3)
    for card in cards:
        if (card.get_color() == HEARTS):
            return True
    return False

def playGame5(cardDealer):
    cards = cardDealer.draw_cards(5)
    sorted(cards, key=Card.get_rank)

    lastCard = cards[0]
    currSeriesLength = 1
    maxSeriesLength = 1
    for i in range(1, 5):
        card = cards[i]
        if (card.get_rank() > lastCard.get_rank()):
            currSeriesLength += 1
            lastCard = card
            maxSeriesLength = max(currSeriesLength, maxSeriesLength)
        else:
            currSeriesLength = 1
            lastCard = card

    return maxSeriesLength >= 3

DEALER = CardDealer()
ITERATION_NBR = 1000000

game1Wins = 0
game2Wins = 0
game3Wins = 0
game4Wins = 0
game5Wins = 0
for i in iter(range(ITERATION_NBR)):
    if (i % 10000 == 0):
        print('iteration ' + str(i))
    game1Wins += 1 if playGame1(DEALER) else 0
    game2Wins += 1 if playGame2(DEALER) else 0
    game3Wins += 1 if playGame3(DEALER) else 0
    game4Wins += 1 if playGame4(DEALER) else 0
    game5Wins += 1 if playGame5(DEALER) else 0
print('game 1 wins = ' + str(game1Wins) + ' -> ' + str(100.*game1Wins / ITERATION_NBR) + '%')
print('game 2 wins = ' + str(game2Wins) + ' -> ' + str(100.*game2Wins / ITERATION_NBR) + '%')
print('game 3 wins = ' + str(game3Wins) + ' -> ' + str(100.*game3Wins / ITERATION_NBR) + '%')
print('game 4 wins = ' + str(game4Wins) + ' -> ' + str(100.*game4Wins / ITERATION_NBR) + '%')
print('game 5 wins = ' + str(game5Wins) + ' -> ' + str(100.*game5Wins / ITERATION_NBR) + '%')
