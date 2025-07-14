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


from pkgutil import get_data
from datetime import datetime as getdate


def determine_100_years(name: str, age: int, repeat: int = 1) -> None:
    resultado = calculo(age)
    print(f'A menssagem sera repetida {repeat}')
    for _ in range(repeat):
        print(f'{name} completará 100 anos em {resultado}')
    print()
    return None
    
    
def calculo(idade: int) -> int:
    ano_atual= getdate.today().year
    #aqui eu to fazendo o calculo do ano que a pessoa vai completar 100 anos
    result = ano_atual + (100 - idade)
    #print(f'{name}, você completará 100 anos em {result}.\n')
    return result
        
     
    

    
    



# Test inputs for determine_100_years
determine_100_years("Alice", 25)
determine_100_years("Bob", 50, 3)
determine_100_years("Charlie", 99, 1)
determine_100_years("Dana", 0, 2)
determine_100_years("Eve", 100, 5)