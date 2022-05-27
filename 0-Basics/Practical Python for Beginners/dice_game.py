import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

p1 = input("Player1 name? ")
p2 = input("Player2 name? ")

def main():
    roll1 = roll_dice()
    roll2 = roll_dice()

    print(p1, 'rolled', roll1)
    print(p2, 'rolled', roll2)

    if roll1>roll2:
        print(p1, 'wins!')
    elif roll1<roll2:
        print(p2, 'wins!')
    else:
        print('You tie!')

main()