"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

def rock_paper_scissors(player1: str, player2: str) -> str:
    pass



























# Test inputs for rock_paper_scissors
print(rock_paper_scissors("rock", "scissors"))    # Player 1 wins
print(rock_paper_scissors("scissors", "paper"))    # Player 1 wins
print(rock_paper_scissors("paper", "rock"))        # Player 1 wins
print(rock_paper_scissors("scissors", "rock"))     # Player 2 wins
print(rock_paper_scissors("paper", "scissors"))    # Player 2 wins
print(rock_paper_scissors("rock", "paper"))        # Player 2 wins
print(rock_paper_scissors("rock", "rock"))         # Tie
print(rock_paper_scissors("paper", "paper"))       # Tie
print(rock_paper_scissors("scissors", "scissors")) # Tie



