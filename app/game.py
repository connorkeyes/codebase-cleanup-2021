
from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(user, comp):
    """
    Chooses winner in rock paper scissors

    Params: user choice, computer choice

    Example: determine_winner("rock", "scissors") returns "rock"
    """
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock"
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors"
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None
        }
    }
    winning_choice = winners[user][comp]
    return winning_choice

if __name__ == "__main__":


    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u, c)

    if winner == u:
        print("YOU WIN!")
    elif winner == c:
        print("COMPUTER WIN!")
    elif winner == None:
        print("IT'S A TIE!")
    
    exit()
