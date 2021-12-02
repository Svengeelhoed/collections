ListOne = [1,2,3,4,5,6,7,8,9,10]
ListTwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists(ListOne, ListTwo):
    for x in range(0,10):
        result = ListOne[x] + ListTwo[x]
        print(str(ListOne[x]) + " + " + str(ListTwo[x]) + " = " + str(result))

def substractAndDisplayLists (ListOne, ListTwo):
    for x in range(0,10):
        result = ListOne[x] - ListTwo[x]
        print(str(ListOne[x]) + " - " + str(ListTwo[x]) + " = " + str(result))

def multiplyAndDisplayLists (ListOne, ListTwo):
    for x in range(0,10):
        result = ListOne[x] * ListTwo[x]
        print(str(ListOne[x]) + " * " + str(ListTwo[x]) + " = " + str(result))

def divideAndDisplayLists (ListOne, ListTwo):
    for x in range(0,10):
        result = ListOne[x] / ListTwo[x]
        print(str(ListOne[x]) + " / " + str(ListTwo[x]) + " = " + str(result))

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'çluedo']

import random
from random import shuffle  
minimum = 3
maximum = 11
def spelProgramma(spelList, minimum, maximum):
    for x in range(random.randint(minimum,maximum)): 
        shuffle(spelList)
        print(spelList[x])

# spelProgramma(spelList, minimum, maximum)

import random
kleuren = ['oranje', 'blauw', 'groen', 'bruin']
# aantal = input("hoeveel m&m's wil je: ")


def zakje(aantal):
    zak = []
    for x in range(int(aantal)):
        zak.append(random.choice(kleuren))
    return zak
print(sorted(zakje(aantal)))
kleuren2 = {'oranje','blauw','groen','bruin'}


def zakje22(amount:int):
    zakje2 = {}
    for i in range(int(amount)):
        kleur = random.choice(kleuren)
        if kleur in zakje2:
            zakje2[kleur] += 1
        else:
            zakje2.update({kleur : 1})
    return zakje2
    
x = input("Hoeveel M&M's wil je in de zak  : ")
print(sorted(zakje22(x).items(), key= lambda kv:kv[1], reverse= True))