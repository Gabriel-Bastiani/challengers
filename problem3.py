"""
Take a list, say for example this one:
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


"""

def filter_less_than_n(lst: list) -> list:
    pass




























# Test inputs for filter_less_than_n
print(filter_less_than_n(a))  # Should return [1, 1, 2, 3]
print(filter_less_than_n([1, 2, 3, 4, 5]))           # All < 5
print(filter_less_than_n([5, 6, 7, 8]))              # None < 5
print(filter_less_than_n([0, -1, 10, 3, 5]))         # Mixed values
print(filter_less_than_n([]))                        # Empty list
print(filter_less_than_n([4, 4, 4, 4]))              # All same, < 5
print(filter_less_than_n([100, 200, 300]))           # All > 5