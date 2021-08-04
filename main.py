# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import dice


def get_unit_stats():
    global WS
    global BS
    global S
    global A

    print("Please enter the units statistics")
    WS = input("WS: ")
    BS = input("BS: ")
    S = input("S: ")
    A = input("A: ")

    print(WS + " " + BS + " " + S + " " + A + " ")

def get_weapon_stats():
    global type
    global WPS
    global D
    global D


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def roll_hits():
    numHitsTotal = []
    numRolls = input("Number of shots the unit gets: ")
    hitRoll = dice.roll(numRolls+'d6')

    for x in range(101):
        numHits = 0
        for roll in hitRoll:
            if roll >= int(WS):
                numHits = numHits + 1
        numHitsTotal.append(numHits)

    averageHits = (sum(numHitsTotal) / len(numHitsTotal))

    print(hitRoll)
    print("Average Number of hits over 100 shooting phases: " + str(averageHits))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_unit_stats()
    roll_hits()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
