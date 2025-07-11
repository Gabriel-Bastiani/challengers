"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

def guess_the_number(user_guess: int, secret_number: int) -> str:
    pass




















# Test inputs for guess_the_number
print(guess_the_number(5, 7))   # Too low
print(guess_the_number(8, 3))   # Too high
print(guess_the_number(4, 4))   # Exactly right
print(guess_the_number(1, 9))   # Too low
print(guess_the_number(9, 1))   # Too high
print(guess_the_number(7, 7))   # Exactly right


