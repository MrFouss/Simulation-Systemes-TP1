#!/usr/bin/python3

from abc import ABCMeta
from card_dealer import * 
import math

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
    cards.sort(key=Card.get_rank)

    lastCard = cards[0]
    currSeriesLength = 1
    maxSeriesLength = 1
    for i in range(1, 5):
        card = cards[i]
        if (card.get_rank() == lastCard.get_rank()+1):
            currSeriesLength += 1
            maxSeriesLength = max(currSeriesLength, maxSeriesLength)
        else:
            currSeriesLength = 1
        lastCard = card

    return maxSeriesLength >= 3

# simulation parameter values

DEALER = CardDealer()
ITERATION_NBR = 1000000
SIMULATION_NBR = 5

# simulation

# gameWinsData[i][j] = succes number for j-th game at i-th simulation
gameWinsData = []

for i in range(SIMULATION_NBR):
    print('----- Simulation number ' + str(i+1) + '/' + str(SIMULATION_NBR))
    gameWins = [0] * 5
    for i in iter(range(ITERATION_NBR)):
        if (i % 10000 == 0):
            print('execution ... ' + str(100. * i / ITERATION_NBR) + '%', end="\r")
        gameWins[0] += 1 if playGame1(DEALER) else 0
        gameWins[1] += 1 if playGame2(DEALER) else 0
        gameWins[2] += 1 if playGame3(DEALER) else 0
        gameWins[3] += 1 if playGame4(DEALER) else 0
        gameWins[4] += 1 if playGame5(DEALER) else 0
    gameWinsData.append(gameWins)
    for j in range(5):
        print('game' + str(j+1) + ' : wins = ' + str(gameWins[j]) + ' -> ' + str(100.*gameWins[j] / ITERATION_NBR) + '%')

# final stats

print('----- Final stats')

# compute average

gameWinsAverage = [0] * 5
for i in range(SIMULATION_NBR):
    for j in range(5):
        gameWinsAverage[j] += gameWinsData[i][j]
for i in range(5):
    gameWinsAverage[i] /= float(SIMULATION_NBR)

# compute standard deviation

gameWinsStdDev = [0] * 5
for i in range(SIMULATION_NBR):
    for j in range(5):
        gameWinsStdDev[j] += pow(gameWinsData[i][j] - gameWinsAverage[j], 2)
for i in range(5):
    gameWinsStdDev[i] = math.sqrt(gameWinsStdDev[i] / float(SIMULATION_NBR))

# print result

for i in range(5):
    print('game' + str(i+1) + ' : avg wins = ' + str(100. * gameWinsAverage[i] / ITERATION_NBR) + '%' + ' ---- std dev wins = ' + str(100. * gameWinsStdDev[i] / ITERATION_NBR) + '%')
