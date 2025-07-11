"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

def determine_100_years(name: str, age: int, repeat: int = 1) -> str:
    pass







# Test inputs for determine_100_years
print(determine_100_years("Alice", 25))
print(determine_100_years("Bob", 50, 3))
print(determine_100_years("Charlie", 99, 1))
print(determine_100_years("Dana", 0, 2))
print(determine_100_years("Eve", 100, 5))