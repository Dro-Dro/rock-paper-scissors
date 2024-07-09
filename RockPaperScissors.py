from random import randint
import sys

#create a win/lose counter for player and computer
pWinCount = 0
cWinCount = 0
pLostCount = 0
cLostCount = 0

#create a list of moves
t = ["Rock", "Paper", "Scissors"]

#set player to false
player = False

#assign a random move to the computer
computer = t[randint(0,2)]

while player == False:
#set player to true
    player = input("\nRock, Paper, Scissors? \n")
    if player == computer:
       print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            pLostCount += 1
            cWinCount += 1
        else:
            print("You win!", player, "smashes", computer)
            pWinCount += 1
            cLostCount += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            pLostCount += 1
            cWinCount += 1
        else:
            print("You win!", player, "covers", computer)
            pWinCount += 1
            cLostCount += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            pLostCount += 1
            cWinCount += 1
        else:
            print("You win!", player, "cuts", computer)
            pWinCount += 1
            cLostCount += 1
    elif player == "Gun":
        print("Nice try buddy.")
    elif player == "End":
        print("Exiting the program...\n")
        sys.exit(0)
    else:
        print("That's not a valid play. Check your spelling!")

    #print current score count
    print("\nCurrent Scores: ")
    print("Player   | Wins: ", pWinCount, " | Losses: ", pLostCount)
    print("Computer | Wins: ", cWinCount, " | Losses: ", cLostCount)
    print("Type 'End' to end the program.")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]