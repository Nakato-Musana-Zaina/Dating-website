
import random
choices = ['rock','paper','scissors']
computer = random.choice(choices)
player = False
cpu_score =0
player_score =0
while True:
    player = input("rock,paper or scissors?").capitalize()
    if player == computer:
        print("tie!")
    elif player=="Rock":
        if computer == "paper":
            print("you lose!", computer, "cover", player)
            cpu_score+=1
        else:
            print("you win", player,"smashes", computer)
            player_score +=1
    elif player == "paper":
        if computer == "scissors":
            print("you lose", computer, "cut",player)
            cpu_score +=1
        else:
            print("you win",player,"cut",computer)
            player_score +=1
    elif player == "scissors":
        if computer == "Rock":
        
            print("You lose...", computer,"smashes",player)
            cpu_score+=1
        else:
            print("you win", player, "cut", computer)
            player_score+=1
    elif player =="end":
        print("final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"player:{player_score}")
        break

    




