from random import randint

"""
Ali Alzurufi

This program is a recreation of the classic game Rock, Paper, Scissors. 
The player will choose between rock, paper, or scissors, and the computer will randomly choose its own option. 
The two choices will be compared to determine the winner, based on the rules that rock beats scissors, paper beats rock, and scissors beats paper. 

Date: 11/03/22

"""


def play_game():
    """
    This function prompts the player to input their selection (rock, paper, or scissors), and displays the computer's random
    selection. If the player wins, the win counter is incremented by 1. If the player loses, the loss counter is incremented 
    by 1. The game will continue to run until the player chooses to exit by entering 4.

    """

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    wins = 0
    losses = 0

    while True:

        try:
            # Prompt the player to enter a numeric selection
            player_selection = int(
                input("Enter 1 for Rock, 2 for Paper, 3 for Scissors, or 4 to Exit: "))
            print()

            # Exit the game if player selects '4'
            if player_selection == 4:
                break

            computer_selection = randint(1, 3)

            # Display player and computer selections
            print(
                f"Your selection: {choices[player_selection]} \nComputer selection: {choices[computer_selection]}")
            print()

            # Determine if the player won, lost, or tied, and increment win/loss counters accordingly
            if player_selection == computer_selection:
                print("It's a draw! Starting again.")
                print()

            elif str(player_selection) + str(computer_selection) in ["13", "21", "32"]:
                print("You Win!")
                print()
                wins += 1

            else:
                print("You Lose.")
                print()
                losses += 1

        # Error handling for invalid input
        except:
            print("Invalid choice. Try again")
            continue

    # Display final game results
    print()
    print(f"Number of wins: {wins}")
    print(f"Number of losses: {losses}")
    print()
    print("Thanks for playing.")


play_game()
