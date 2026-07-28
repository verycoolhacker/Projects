#script import
import random
import time
#start loop
while True:
    rpsoption = ("rock", "paper", "scissors")
    valid_options = ["rock", "paper", "scissors"]
    #setting beginning player response to non and computer randomizer
    player = None
    computer = random.choice(rpsoption)
    #player input
    player = input("Pick one (Rock, Paper, Scissors):")
    #checking for correct response
    if player not in valid_options:
        print("Error incorrect response")
        time.sleep(1)
        continue
    #final verdict
    print(f"player: {player}")
    print(f"computer: {computer}")

    time.sleep(2)

#please do not steal, thx! :D