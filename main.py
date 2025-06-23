
import random

'''
1 for snake 
-1 for water 
0 for gun
'''

youdict = {"s": 1 , "w": -1 , "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Input from user
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Validate user input
if youstr not in youdict:
    print("Invalid input!")
else:
    you = youdict[youstr]
    computer = random.choice([-1, 0, 1])

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if you == computer:
        print("It's a draw!")

    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")

    else:
        print("You lose!")

       








