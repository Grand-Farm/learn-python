import random
# game you need to play tree times to find the winner.

number_play = int(input("How many time you want to play: "))
for i in range(number_play):
    computer = random.choice(["paper", "rock", "scissor"])
    guest = (input("Do you want rock, paper, scissor "))
    if computer == guest:
        print("Tie, play again ", computer)
    elif computer == "rock" and guest == "paper":
        print("The winner is guest", computer)
    elif computer == "scissor" and guest == "rock":
        print("The winner is guest", computer)
    elif computer == "paper" and guest == "scissor":
        print("The winner is guest", computer)
    else:
        print("The winner is computer", computer)
