import random

def Roll_dice():
    roll = input('Roll the dice? [Yes or No]: ')

    while roll.lower() == 'Yes'.lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)

        print('dice rolled: {} and {}'.format(dice1,dice2))

        roll = input('Roll again? [Yes or No]: ')
Roll_dice()        