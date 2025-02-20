"""
Author: Santiago Bergerat

Purpose: Practice finding items in lists.
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999  # Valor alto inicial
youngest_name = ""   # Variable para el nombre del más joven

for gente in people:
    print(gente)
    parts = gente.split(" ")

    name = parts[0]
    age = int(parts[1]) 

    print(f'The name is {name} and the age is: {age}')

    if age < youngest_age:
        youngest_age = age
        youngest_name = name  

print(f"\nThe youngest person is: {youngest_name} with an age of {youngest_age}")
