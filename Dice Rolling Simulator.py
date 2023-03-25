import random

def roll_dice():

    dice_drawing = {
        1: (
        " _______",
        "|       |",
        "|   O   |",
        "[_______]",
        ),
        2: (
        " _______",
        "|       |",
        "|  O O  |",
        "[_______]",
        ),
        3: (
        " _______",
        "|       |",
        "|   O   |",
        "|  O O  |",
        "[_______]",
        ),
        4: (
        " _______",
        "|       |",
        "|  O O  |",
        "|  O O  |",
        "[_______]",
        ),
        5: (
        " _______",
        "|       |",
        "|  O O  |",
        "| O O O |",
        "[_______]",
        ),
        6: (
        " _______",
        "|       |",
        "| O O O |",
        "| O O O |",
        "[_______]",
        ),
    }
    roll = input("Do you want to roll dice? (yes/no) ")

    while roll.lower() == "yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        roll = input("Roll again? (yes/no) ")

roll_dice()