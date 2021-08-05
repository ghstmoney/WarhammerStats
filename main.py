# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import dice


def get_unit_stats():
    global WS
    global BS
    global S
    global T
    global A

    print("Please enter the units statistics")
    WS = input("WS: ")
    BS = input("BS: ")
    T = input("T: ")
    S = input("S: ")
    A = input("A: ")

def get_weapon_stats():
    global type
    global WPS
    global D
    global AP

    print("Please enter the weapon statistics")
    WPS = input("WPS: ")
    D = input("D: ")
    # S = input("AP: ")
    # A = input("A: ")

def roll_hits():
    global averageHits

    numHitsTotal = []
    numRolls = input("Number of shots the unit gets: ")


    for x in range(1001):
        hitRoll = dice.roll(numRolls + 'd6')
        numHits = 0
        for roll in hitRoll:
            if roll >= int(WS):
                numHits = numHits + 1
        numHitsTotal.append(numHits)

    averageHits = (sum(numHitsTotal) / len(numHitsTotal))

    print(hitRoll)
    print("Average Number of hits over 1000 shooting phases: " + str(averageHits))

def calc_wounds():
    damageTable = []

    #calculate the wounds for toughness 1 through 17
    for toughness in range(17):
        wounds = 0

        for woundRoll in range(1001):
            #figure out the roll needed for a successful wound

            # If the weapon strength is half of the toughness wounds on a 6 up
            if int(WPS) < toughness and int(WPS) / toughness <= .5:
                diceRoll = dice.roll("1d6")
                if diceRoll[0] >= 6:
                    wounds = wounds + 1
                continue

            # If the weapon strength less than the toughness wounds on a 5 up
            if int(WPS) < toughness:
                diceRoll = dice.roll("1d6")
                if diceRoll[0] >= 5:
                    wounds = wounds + 1
                continue

            # If the weapon strength equals the toughness wounds on a 4 up
            if int(WPS) == toughness:
                diceRoll = dice.roll("1d6")
                if diceRoll[0] >= 4:
                    wounds = wounds + 1
                continue

            # If the weapon strength is greater than the toughness wound on a 3 up
            if int(WPS) > toughness:
                diceRoll = dice.roll("1d6")
                if diceRoll[0] >= 3:
                    wounds = wounds + 1
                continue

            # If the weapon strength is double the toughness wound on a 2 up
            if int(WPS) > toughness and int(WPS) / toughness >= 2:
                diceRoll = dice.roll("1d6")
                if diceRoll[0] >= 2:
                    wounds = wounds + 1
                continue

        damageTable.append(wounds)

    print(damageTable)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_unit_stats()
    roll_hits()
    get_weapon_stats()
    calc_wounds()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
