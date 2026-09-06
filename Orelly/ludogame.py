import sys
from random import randint

if len(sys.argv) <2:
    sys.exit("Please enter player name")

player_name = sys.argv[1]

def check_winner(player,dice):
    print("dice: ",dice)
    if dice == 6:
        print(player," own")
    else:
        print("better luck next time",player)


check_winner(player_name,randint(1,6))
