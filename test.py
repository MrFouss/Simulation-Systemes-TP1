from card_dealer import * 
import itertools

def allCombinations() :
    list = []

    for i in range(52) :
        list.append(Card(i))

    return itertools.combinations(list, 5)

def containsSeries(tuple):
    checkSeries = [0]*13

    for c in tuple :
        checkSeries[c.get_rank()] += 1
    
    seriesLen = 0
    for i in checkSeries :
        if (i > 0) :
            seriesLen += 1
            if (seriesLen >= 3) :
                return True
        else :
            seriesLen = 0
    
    return False

all = list(allCombinations())

print("5 cards combinations = " + str(len(all)))

count = 0
for t in all :
    if (containsSeries(t)) :
        count += 1

print("5 card combinations containing a series of at least 3 consecutive ranks = " + str(count))

print("percentage -> = " + str(100.*count/len(all)) + " %")
