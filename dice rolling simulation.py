# creating the dice rolling simulation

import random


def roll_dice():

    dice_drawing = {
        1: (
            " _____ ",
            "|  1  |",
            "|  o  |",
            "|_____|",
        ),
        2: (
            " _____",
            "|o    |",
            "|  2  |",
            "|    o|",
            "|_____|",
        ),
        3: (
            " ______",
            "|o  3  |",
            "|  o   |",
            "|    o |",
            "|______|",
        ),
        4: (
            " _____",
            "|o   o|",
            "|  4  |",
            "|o   o|",
            "|_____|",
        ),
        5: (
            " ______",
            "|o 5  o|",
            "|  o   |",
            "|o    o|",
            "|______|",
        ),
        6: (
            " _______ ",
            "|o    o |",
            "|o 6  o |",
            "|o    o |",
            "|_______|",
        ),
    }

    roll = input("roll the dice ? (YES/ NO):")

    while roll.lower() == "YES".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("roll again ? (YES/NO): ")


roll_dice()
