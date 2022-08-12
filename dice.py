import random


def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


def main():
    play1 = input("Enter name1: ")
    play2 = input("Enter name2: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(play1, 'rolled', roll1)
    print(play2, 'rolled', roll2)
    if roll1 > roll2:
        print("play1 win")
    elif roll1 == roll2:
        print("not winner")
    else:
        print("play2 win")
main()