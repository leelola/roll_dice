import random
import time

roll_dice = "yes"

while roll_dice == "yes" or roll_dice == "y":
    print("\nRolling the dice..")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("the values are:")
    print("Dice 1 =",dice1, "\nDice 2=", dice2)

    if dice1==dice2:
        print ("You rolled a double")
    else:
        print("Keep playing")

        roll_again = input("\nRoll the dice again? (Y/N) ")

 
